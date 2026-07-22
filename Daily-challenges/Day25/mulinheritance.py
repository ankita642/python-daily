class CoreRepository:
    def save(self, data):
        print(f"Saving data to DB: {data}")

class LoggingMixin(CoreRepository):
    def save(self, data):
        print("[LOG] Audit trail updated")
        super().save(data)

class ValidationMixin(CoreRepository):
    def save(self, data):
        if not data:
            raise ValueError("Data cannot be empty")
        print("[VALIDATION] Data passed checks")
        super().save(data)

# The Architectural Problem: Ordering Matters
class SecureRepository(ValidationMixin, LoggingMixin):
    pass

repo = SecureRepository()
repo.save("User Record")
