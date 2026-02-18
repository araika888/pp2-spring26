#1
class Flyer:
    def fly(self):
        return "Flying..."


class Swimmer:
    def swim(self):
        return "Swimming..."


class Duck(Flyer, Swimmer):
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Duck: {self.name}"


duck = Duck("Donald")
print("1)", duck.info())
print("1)", duck.fly())
print("1)", duck.swim())

#2
class Printer:
    def print_doc(self, text):
        return f"Printing: {text}"


class Scanner:
    def scan(self):
        return "Scanning..."


class AllInOne(Printer, Scanner):
    pass


aio = AllInOne()
print("2)", aio.print_doc("My homework"))
print("2)", aio.scan())

#3
from datetime import datetime

class LoggerMixin:
    logs = []

    def log(self, msg):
        self.logs.append(msg)


class TimestampMixin:
    def now(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class AppLogger(LoggerMixin, TimestampMixin):
    def log(self, msg):
        stamped = f"[{self.now()}] {msg}"
        self.logs.append(stamped)

    @classmethod
    def show_logs(cls):
        return cls.logs


logger = AppLogger()
logger.log("User logged in")
logger.log("File uploaded")
print("3)", *AppLogger.show_logs(), sep="\n   ")

#4
class ElectricMixin:
    def __init__(self, *args, battery_kwh=0, **kwargs):
        super().__init__(*args, **kwargs)
        self.battery_kwh = battery_kwh

    def charge(self, kwh):
        if kwh <= 0:
            return "kWh must be positive"
        self.battery_kwh += kwh
        return f"Charged +{kwh} kWh"


class GasMixin:
    def __init__(self, *args, fuel_liters=0, **kwargs):
        super().__init__(*args, **kwargs)
        self.fuel_liters = fuel_liters

    def refuel(self, liters):
        if liters <= 0:
            return "Liters must be positive"
        self.fuel_liters += liters
        return f"Refueled +{liters} L"


class HybridCar(ElectricMixin, GasMixin):
    def __init__(self, brand, model, battery_kwh=0, fuel_liters=0):
        self.brand = brand
        self.model = model
        super().__init__(battery_kwh=battery_kwh, fuel_liters=fuel_liters)

    def status(self):
        return f"{self.brand} {self.model} | Battery: {self.battery_kwh} kWh | Fuel: {self.fuel_liters} L"


car = HybridCar("Toyota", "Prius", battery_kwh=10, fuel_liters=20)
print("4)", car.status())
print("4)", car.charge(5))
print("4)", car.refuel(10))
print("4)", car.status())

#5
class StudentBase:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.study_hours = 0

    def study(self, subject, hours):
        if hours <= 0:
            return "Hours must be positive"
        self.study_hours += hours
        return f"Studied {subject} for {hours} hour(s)"


class WorkerBase:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.work_hours = 0

    def work(self, hours):
        if hours <= 0:
            return "Hours must be positive"
        self.work_hours += hours
        return f"Worked for {hours} hour(s)"


class WorkingStudent(StudentBase, WorkerBase):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def report(self):
        return f"{self.name} | Study hours: {self.study_hours} | Work hours: {self.work_hours}"


ws = WorkingStudent("Madina")
print("5)", ws.study("Math", 2))
print("5)", ws.work(4))
print("5)", ws.report())

#6
class AuthMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_logged_in = False
        self.username = None

    def login(self, username, password):
        if password == "admin123":
            self.is_logged_in = True
            self.username = username
            return "Login successful"
        return "Login failed"


class PermissionMixin:
    def has_permission(self, action):
        if action == "delete":
            return getattr(self, "is_logged_in", False) is True
        return True


class AdminUser(AuthMixin, PermissionMixin):
    def __init__(self, full_name):
        self.full_name = full_name
        super().__init__()

    def whoami(self):
        return f"AdminUser: {self.full_name} (logged_in={self.is_logged_in})"


admin = AdminUser("Madina T.")
print("6)", admin.whoami())
print("6)", admin.login("madina", "wrong"))
print("6)", "can delete?", admin.has_permission("delete"))
print("6)", admin.login("madina", "admin123"))
print("6)", "can delete?", admin.has_permission("delete"))

#7
class Camera:
    def take_photo(self):
        return "📸 Photo taken"


class Phone:
    def make_call(self, number):
        return f"📞 Calling {number}..."


class GPS:
    def get_location(self):
        return "📍 Location: 43.2389, 76.8897"


class Smartphone(Camera, Phone, GPS):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"Smartphone: {self.brand} {self.model}"


sp = Smartphone("Samsung", "S24")
print("7)", sp.info())
print("7)", sp.take_photo())
print("7)", sp.make_call("+77001234567"))
print("7)", sp.get_location())