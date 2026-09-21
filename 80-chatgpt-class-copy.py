"""
QUICK REFERENCE GUIDE - ALL 10 EXAMPLES
Ek diagram mein sab kuch
"""

print("""
╔══════════════════════════════════════════════════════════════════════════╗
║                    QUICK REFERENCE GUIDE - ALL 10                       ║
╚══════════════════════════════════════════════════════════════════════════╝


LEVEL 1 - EASY
══════════════════════════════════════════════════════════════════════════

┌─ EXAMPLE 1A: Student (String)         ─ EXAMPLE 1B: Car (Numeric) ─┐
│                                                                       │
│ class Student:                       │ class Car:                  │
│   @property                          │   @property                 │
│   def name(self):                    │   def speed(self):          │
│     return self._name                │     return self._speed      │
│                                      │                             │
│   @name.setter                       │   @speed.setter             │
│   def name(self, value):             │   def speed(self, value):   │
│     if len(value) < 2:               │     if not (0 <= value <= 200):
│       raise ValueError()             │       raise ValueError()    │
│     self._name = value.upper()       │     self._speed = value     │
│                                      │                             │
│ ✓ String validation + transform      │ ✓ Numeric range validation │
│ ✓ Simple single check                │ ✓ Min/Max bounds           │
│                                      │                             │
│ use_case: Form field         │ use_case: Speed control     │
└────────────────────────────────────────────────────────────────────────┘


LEVEL 2 - EASY-MEDIUM
══════════════════════════════════════════════════════════════════════════

┌─ EXAMPLE 2A: BankAccount (Finance)   ─ EXAMPLE 2B: Product (Ecommerce) ─┐
│                                                                           │
│ class BankAccount:                   │ class Product:                    │
│   def __init__(self, holder, bal):   │   def __init__(self, name, p, s): │
│     self.account_holder = holder     │     self.name = name              │
│     self.balance = balance           │     self.price = price            │
│                                      │     self.stock = stock            │
│   @property                          │                                   │
│   def balance(self):                 │   @property                       │
│     return self._balance             │   def stock(self):                │
│                                      │     return self._stock            │
│   @balance.setter                    │                                   │
│   def balance(self, value):          │   def buy(self, qty):             │
│     if value < 0:                    │     if qty > self.stock:          │
│       raise ValueError()             │       return False                │
│     self._balance = value            │     self.stock -= qty             │
│                                      │                                   │
│ ✓ Multiple independent properties    │ ✓ Business logic (buy method)     │
│ ✓ Different validation per prop      │ ✓ State manipulation              │
│                                      │                                   │
│ use_case: Banking      │ use_case: Shopping           │
└───────────────────────────────────────────────────────────────────────────┘


LEVEL 3 - MEDIUM
══════════════════════════════════════════════════════════════════════════

┌─ EXAMPLE 3A: Temperature (Math)      ─ EXAMPLE 3B: Battery (Status) ─┐
│                                                                        │
│ class Temperature:                   │ class MobilePhone:             │
│   @property                          │   @property                    │
│   def celsius(self):                 │   def battery_percentage(self):│
│     return self._celsius             │     return self._battery       │
│                                      │                                │
│   @celsius.setter                    │   @property                    │
│   def celsius(self, value):          │   def is_low(self):            │
│     if value < -273.15:              │     return self._battery < 20  │
│       raise ValueError()             │                                │
│     self._celsius = value            │   @property                    │
│                                      │   def battery_status(self):    │
│   @property                          │     if self.is_critical:       │
│   def fahrenheit(self):  # NO SETTER │       return "🔴 CRITICAL"   │
│     return (self._celsius * 9/5) + 32│     elif self.is_low:          │
│                                      │       return "🟠 LOW"         │
│   @property                          │     return "🟢 FULL"          │
│   def kelvin(self):  # NO SETTER     │                                │
│     return self._celsius + 273.15    │ ✓ Multiple calculated props    │
│                                      │ ✓ Status determination logic   │
│ ✓ Getter-only properties             │ ✓ Boolean-based calculations   │
│ ✓ Mathematical conversions           │ ✓ User-friendly strings        │
│                                      │                                │
│ use_case: Unit convert    │ use_case: Device monitor   │
└────────────────────────────────────────────────────────────────────────┘


LEVEL 4 - MEDIUM-HARD
══════════════════════════════════════════════════════════════════════════

┌─ EXAMPLE 4A: Rectangle (Geometry)   ─ EXAMPLE 4B: Employee (Salary) ─┐
│                                                                        │
│ class Rectangle:                     │ class Employee:                │
│   @property                          │   @property                    │
│   def width(self):                   │   def base_salary(self):       │
│     return self._width               │     return self._base_salary   │
│                                      │                                │
│   @width.setter                      │   @property                    │
│   def width(self, value):            │   def bonus_amount(self):      │
│     if value <= 0:                   │     # DEPENDS ON BONUS %       │
│       raise ValueError()             │     return (self._base_salary  │
│     self._width = value              │             * self._bonus_pct) │
│                                      │                                │
│   @property                          │   @property                    │
│   def area(self):  # DEPENDS ON W,H  │   def tax(self):               │
│     return self._width * self._height│     # DEPENDS ON SALARY        │
│                                      │     total = self.base_salary + │
│   @property                          │            self.bonus_amount   │
│   def is_square(self):               │     return total * 0.10        │
│     # BOOLEAN CALC                   │                                │
│     return self._width == self._height│  @property                    │
│                                      │   def net_salary(self):        │
│ ✓ Properties depend on each other    │     # COMPLEX CALCULATION      │
│ ✓ Multiple calculation chains        │     return (self.base_salary + │
│ ✓ Boolean-based properties           │             self.bonus_amount -│
│ ✓ Geometric relationships            │             self.tax)         │
│                                      │                                │
│ use_case: Geometry calc    │ use_case: Payroll system   │
└────────────────────────────────────────────────────────────────────────┘


LEVEL 5 - HARD
══════════════════════════════════════════════════════════════════════════

┌─ EXAMPLE 5A: UserProfile (Auth)     ─ EXAMPLE 5B: SocialMedia (Verify) ─┐
│                                                                           │
│ class UserProfile:                   │ class SocialMediaAccount:         │
│   def __init__(self, user, email):   │   MIN_AGE = 13                    │
│     self.username = username         │   FOLLOWER_MILESTONE = 1000       │
│     self._login_attempts = 0         │                                   │
│                                      │   def __init__(self, user, em):   │
│   @property                          │     self.username = user          │
│   def username(self):                │     self._followers = 0           │
│     return self._username            │     self._is_verified = False     │
│                                      │                                   │
│   @username.setter                   │   @property                       │
│   def username(self, value):         │   def can_verify(self):           │
│     if not self._is_valid_username() │     # MULTIPLE CONDITIONS        │
│       raise ValueError()             │     return (self.followers >=    │
│     self._username = value           │             self.FOLLOWER_MILESTONE│
│                                      │             and self.age >= 18)  │
│   def _is_valid_username(self, val): │                                   │
│     # PRIVATE METHOD - Complex logic │   @followers.setter              │
│     if len(val) < 3 or len > 20:    │   def followers(self, value):     │
│       return False                   │     old = self._followers         │
│     if not all(c.isalnum()...):      │     self._followers = value       │
│       return False                   │     # CHECK MILESTONE             │
│     return True                      │     if old < MILESTONE <= value:  │
│                                      │       print("Congratulations!")   │
│   def attempt_login(self, pwd):      │                                   │
│     if self.is_locked:               │   def verify_account(self):       │
│       return False                   │     if not self.can_verify:       │
│     if pwd == "correct":             │       return False                │
│       self._login_attempts = 0       │     self._is_verified = True      │
│     else:                            │     return True                   │
│       self._login_attempts += 1      │                                   │
│                                      │ ✓ Class constants (best practice)│
│   @property                          │ ✓ Complex eligibility logic      │
│   def is_locked(self):               │ ✓ Threshold-based verification   │
│     return self._login_attempts >= 3│ ✓ Milestone tracking             │
│                                      │                                   │
│ ✓ Private validation methods        │ ✓ Multiple validation layers     │
│ ✓ State management (counter)        │ ✓ Complex business logic         │
│ ✓ Account locking mechanism         │ ✓ Eligibility checking           │
│                                      │                                   │
│ use_case: User auth      │ use_case: Platform verification │
└───────────────────────────────────────────────────────────────────────────┘


═══════════════════════════════════════════════════════════════════════════


QUICK LOOKUP TABLE: Kaunsi example kaunse feature mein use hoti hai?
═══════════════════════════════════════════════════════════════════════════

                                        FIRST SET    NEW SET
────────────────────────────────────────────────────────────────────────
SIMPLE VALIDATION                       1A-Student   1B-Car
STRING TRANSFORMATION (.upper())        1A-Student   ❌
RANGE VALIDATION (min/max)              ❌           1B-Car
MULTIPLE INDEPENDENT PROPERTIES         2A-Bank      2B-Product
BUSINESS LOGIC METHODS                  2A-Bank      2B-Product
MATHEMATICAL CONVERSIONS                3A-Temp      ❌
STATUS/STATE DETERMINATION              ❌           3B-Battery
BOOLEAN CALCULATED PROPERTIES           4A-Rect      3B-Battery
DEPENDENT CALCULATIONS                  4A-Rect      4B-Employee
FINANCIAL CALCULATIONS                  ❌           4B-Employee
PRIVATE VALIDATION METHODS              5A-User      5B-Social
STATE MANAGEMENT (counters)             5A-User      5B-Social
ACCOUNT LOCKING/SECURITY                5A-User      ❌
VERIFICATION THRESHOLDS                 ❌           5B-Social
CLASS CONSTANTS (best practice)         ❌           5B-Social
MILESTONE TRACKING                      ❌           5B-Social


═══════════════════════════════════════════════════════════════════════════


COPY-PASTE TEMPLATES - Apne code mein use kar!
═══════════════════════════════════════════════════════════════════════════

TEMPLATE 1: SIMPLE VALIDATION
────────────────────────────
@property
def age(self):
    return self._age

@age.setter
def age(self, value):
    if value < 0 or value > 150:
        raise ValueError("Age valid nahi hai")
    self._age = value


TEMPLATE 2: STRING VALIDATION + TRANSFORM
──────────────────────────────────────────
@property
def email(self):
    return self._email

@email.setter
def email(self, value):
    if '@' not in value:
        raise ValueError("Invalid email")
    self._email = value.lower()  # Transform


TEMPLATE 3: GETTER-ONLY (CALCULATED)
───────────────────────────────────
@property
def full_name(self):  # NO SETTER
    return f"{self._first} {self._last}"

@property
def age_group(self):  # NO SETTER
    if self._age < 13:
        return "Child"
    return "Adult"


TEMPLATE 4: DEPENDENT PROPERTIES
─────────────────────────────────
@property
def total_price(self):  # Depends on quantity + unit_price
    return self._quantity * self._unit_price

@property
def tax(self):  # Depends on total_price
    return self.total_price * 0.10

@property
def final_price(self):  # Depends on multiple
    return self.total_price + self.tax


TEMPLATE 5: PRIVATE VALIDATION METHOD
──────────────────────────────────────
def _is_valid_phone(self, value):
    # Private method - internal use only
    if len(value) != 11:
        return False
    if not value.isdigit():
        return False
    return True

@property
def phone(self):
    return self._phone

@phone.setter
def phone(self, value):
    if not self._is_valid_phone(value):
        raise ValueError("Phone invalid hai")
    self._phone = value


═══════════════════════════════════════════════════════════════════════════


HOW TO CHOOSE WHICH EXAMPLE TO STUDY
═════════════════════════════════════

PROBLEM                           → STUDY THIS EXAMPLE
──────────────────────────────────────────────────────────────────
1. "Ek property ko validate karna     → LEVEL 1 (1A or 1B)
    hai"

2. "Multiple properties ho, sab ka     → LEVEL 2 (2A or 2B)
    apna validation ho"

3. "Calculated values chahiye jo       → LEVEL 3 (3A or 3B)
    read-only hon"

4. "Properties aik-dusre ko affect     → LEVEL 4 (4A or 4B)
    karti hon"

5. "Pura complex system bana raha      → LEVEL 5 (5A or 5B)
    hoon"


═══════════════════════════════════════════════════════════════════════════


NEXT STEP: PRACTICE!
════════════════════

1️⃣  PICK AN EXAMPLE
   └─ Choose one that interests you

2️⃣  RUN IT
   └─ python getter_setter_5_examples.py

3️⃣  MODIFY IT
   └─ Change values, add validation

4️⃣  CREATE YOUR OWN
   └─ Think of your use case
   └─ Pick appropriate pattern
   └─ Code it!

5️⃣  COMMON USE CASES:
   ├─ Library Management System
   ├─ School Fee Calculator
   ├─ Weather App
   ├─ Gaming Score System
   ├─ Food Delivery App
   └─ More!


═══════════════════════════════════════════════════════════════════════════

NOW YOU HAVE 10 COMPLETE EXAMPLES! 🎉

Har level par do-do examples, real-world use cases, aur detailed
explanations. Start chote examples se aur ache se samajh lo!

Good Luck! 💯

═══════════════════════════════════════════════════════════════════════════
""")