DEFAULT_SEARCH_FIELD = "from"


class DataStore:
    store_count = 0

    def __init__(self, store_name):
        DataStore.store_count += 1
        self.store_name = store_name
        self.records = []

    def add(self, record_dict):
        try:
            if not isinstance(record_dict, dict):
                raise ValueError("Records must be of type dictionaries")
            self.records.append(record_dict)
            print(f"[{self.store_name}] Added : {record_dict}")
        except ValueError as error:
            print(f"[{self.store_name}] Add failed : {error}")

    def search(self, query_value, field=DEFAULT_SEARCH_FIELD):
        """Return all records where the specified field contains the query value."""
        matching_records = [
            record
            for record in self.records
            if query_value.lower() in str(record.get(field, "").lower())
        ]
        return matching_records

    def delete(self, query_value, field=DEFAULT_SEARCH_FIELD):
        """Remove all records where the specified field matches the query value."""
        original_count = len(self.records)
        self.records = [
            record
            for record in self.records
            if query_value.lower() not in str(record.get(field, "").lower())
        ]
        deleted_count = original_count - len(self.records)
        print(
            f"[{self.store_name}] Deleted {deleted_count} record(s) matching '{query_value}'."
        )

    def list_all(self):
        """Print every record in the store with its index number."""
        if not self.records:
            print(f"[DataStore '{self.store_name}'] No records stored yet.")
            return
        print(
            f"\n[DataStore '{self.store_name}'] All records ({len(self.records)} total):"
        )
        for index, record in enumerate(self.records, start=1):
            print(f"  {index}. {record}")


class ConversionLog(DataStore):
    """Inherits DataStore — same storage engine, smarter API for unit conversions.
        OOP features in this class:
        INHERITED  — search(), delete()          unchanged from DataStore
        OVERRIDDEN — list_all()                  same name, conversion-specific formatting
        NEW        — log_conversion(), summary() brand-new behaviour not in DataStore

    Callbacks to the Smart Unit Converter built in Session 03.
    """

    def __init__(self, session_name):
        """Set up a conversion log that also counts total conversions performed."""
        # super().__init__() runs DataStore.__init__() first — ALWAYS before anything else.
        # This creates self.records and self.store_name, and increments store_count.
        super().__init__(store_name=f"conversions_{session_name}")

        # Child-only instance variables — DataStore does not have these
        self.session_name = session_name
        self.conversion_count = 0

    def log_conversion(self, input_value, input_unit, output_value, output_unit):
        """NEW — builds the conversion dict for you, then reuses inherited DataStore.add()."""
        self.conversion_count += 1
        conversion_record = {
            "from": f"{input_value} {input_unit}",
            "to": f"{output_value:.2f} {output_unit}",
        }
        self.add(conversion_record)  # inherited — zero rewriting

    def list_all(self):
        """OVERRIDE — replaces DataStore.list_all() with conversion-specific formatting.

        Same method name as the parent. Python calls THIS version when the object
        is a ConversionLog. DataStore objects still use DataStore.list_all().
        """
        if not self.records:
            print(f"[ConversionLog] '{self.session_name}': No conversions yet.")
            return
        print(
            f"\n[ConversionLog] '{self.session_name}' "
            f"— {len(self.records)} conversion(s):"
        )
        for i, r in enumerate(self.records, 1):
            print(f"  {i}.  {r['from']}  →  {r['to']}")

    def summary(self):
        """NEW — prints a one-line count of conversions logged this session."""
        print(
            f"\n[ConversionLog] Session '{self.session_name}': "
            f"{self.conversion_count} conversion(s) logged."
        )


class TemperatureLog(DataStore):
    """Inherits from DataStore. Logs temperature conversions in a clean format."""

    def __init__(self, location_name):
        super().__init__(store_name=f"temperatures_{location_name}")
        self.location_name = location_name
        self.temp_count = 0

    def log_temp(self, celsius):
        self.temp_count += 1
        fahrenheit = (celsius * 9 / 5) + 32
        record = {"celsius": celsius, "fahrenheit": fahrenheit}
        self.add(record)

    def list_all(self):
        if not self.records:
            print(f"[TemperatureLog] '{self.location_name}': No temps logged yet.")
            return
        print(
            f"\n[TemperatureLog] '{self.location_name}' — {len(self.records)} reading(s):"
        )
        for i, r in enumerate(self.records, 1):
            print(f" {i}. {r['celsius']}°C → {r['fahrenheit']:.1f}°F")
        # This is method overriding: same method name, different behaviour.

    def summary(self):
        print(
            f"\n[TemperatureLog] Location '{self.location_name}': {self.temp_count} reading(s) total."
        )


# ── DEMO RUN ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":

    # ── CLASS VARIABLE: shared across all instances ───────────────────────────
    print("=" * 55)
    print("CLASS VARIABLE: DataStore.store_count")
    print("=" * 55)
    print(f"Stores created so far: {DataStore.store_count}")  # 0 — no objects yet

    # ── ACT 1: DataStore — raw dicts added manually ───────────────────────────
    # Notice we manually build the dict every time. That repetition is the
    # problem ConversionLog solves in Act 2.
    print("\n" + "=" * 55)
    print("ACT 1: DataStore — storing conversion records manually")
    print("=" * 55)

    store = DataStore("unit_conversions")
    print(f"Stores created so far: {DataStore.store_count}")  # 1

    store.add({"from": "5.0 kg", "to": "11.02 lb"})
    store.add({"from": "10.0 km", "to": "6.21 miles"})
    store.add({"from": "100.0 C", "to": "212.00 F"})

    # exercise: adding  more objects
    store.add({"from": "25.0 C", "to": "77.00 F"})
    store.add({"from": "8.0 km", "to": "4.8 miles"})
    store.add({"from": "6.0 lb", "to": "2.72 kg "})
    store.add("jiugv")

    store.list_all()  # DataStore.list_all() — raw dict format

    print("\n── Search for 'kg' (default field: 'from') ──")
    results = store.search("kg")
    for r in results:
        print(f"  Found: {r}")

    # search for lb to find records with lb in from field
    print("\n── Search for 'lb' (default field: 'from') ──")
    results = store.search("lb")
    for r in results:
        print(f"  Found: {r}")

    print("\n── Delete 'km' record ──")
    store.delete("km")
    store.list_all()

    # Note: saving to a file is Session 06 — File Handling + Data Formats

    # ── ACT 2: ConversionLog — inherit + override + new ───────────────────────
    print("\n" + "=" * 55)
    print("ACT 2: ConversionLog — cleaner API, overridden list_all()")
    print("  (callbacks to Session 03 Smart Unit Converter)")
    print("=" * 55)

    log = ConversionLog("morning_session")
    print(
        f"Stores created so far: {DataStore.store_count}"
    )  # 2 — super().__init__() fired

    log.log_conversion(5.0, "kg", 11.02, "lb")  # no manual dict — log_conv handles it
    log.log_conversion(10.0, "km", 6.21, "miles")
    log.log_conversion(100.0, "C", 212.00, "F")

    log.list_all()  # ConversionLog.list_all() — OVERRIDDEN, cleaner output
    log.summary()  # new method — exists only in ConversionLog

    print("\n── Inherited search — find all 'kg' records ──")
    kg_results = log.search("kg")  # search() inherited unchanged from DataStore
    for r in kg_results:
        print(f"  Found: {r}")

    # Part C: Test TemperatureLog
    temp_log = TemperatureLog("New York")
    print(f"Stores created: {DataStore.store_count}")
    # Should be 3(DataStore + ConversionLog + TemperatureLog)
    # Log some temperatures
    temp_log.log_temp(0)  # Freezing point
    temp_log.log_temp(100)  # Boiling point
    temp_log.log_temp(37)  # Body temperature
    # Call your overridden list_all()
    temp_log.list_all()
    # # Call your new summary() method
    temp_log.summary()

    # PART D: # ── CLASS VARIABLE: final proof — shared by class and all instances
    print(f"\nDataStore.store_count (via class): {DataStore.store_count}")
    print(f"store.store_count (via DataStore object): {store.store_count}")
    print(f"log.store_count (via ConversionLog object): {log.store_count}")
    print(f"temp_log.store_count (via TemperatureLog object): {temp_log.store_count}")
