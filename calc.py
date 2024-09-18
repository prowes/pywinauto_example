# C:\Users\IOS004\AppData\Local\Programs\Python\Python312\Scripts\pytest.exe

from pywinauto import Application, Desktop

auto_ids_dict = {
    "1": "num1Button",
    "2": "num2Button",
    "+": "plusButton",
    "-": "minusButton",
    "=": "equalButton",
    "results": "CalculatorResults",
    "close": "Close",
    "open_menu": "TogglePaneButton",
    "settings": "SettingsItem",
    "send_feedback": "FeedbackButton"
}

def test_one_adding():
    app = Application(backend="uia").start("calc.exe")
    # app = Application(backend="uia").connect(title="Calculator")
    dlg = Desktop(backend="uia").Calculator
    dlg.child_window(auto_id=auto_ids_dict["1"]).click()
    dlg.child_window(auto_id=auto_ids_dict["+"]).click()
    dlg.child_window(auto_id=auto_ids_dict["2"]).click()
    dlg.child_window(auto_id=auto_ids_dict["="]).click()
    results = dlg.child_window(auto_id=auto_ids_dict["results"]).texts()[0]
    assert int(results.split(" ")[-1]) == 3  # show in inspect
    dlg.child_window(auto_id=auto_ids_dict["close"]).click()
    dlg.wait_not("visible")


def test_two_substracting():
    app = Application(backend="uia").start("calc.exe")
    dlg = Desktop(backend="uia").Calculator
    dlg.child_window(auto_id=auto_ids_dict["1"]).click()
    dlg.child_window(auto_id=auto_ids_dict["-"]).click()
    dlg.child_window(auto_id=auto_ids_dict["2"]).click()
    dlg.child_window(auto_id=auto_ids_dict["="]).click()
    results = dlg.child_window(auto_id=auto_ids_dict["results"]).texts()[0]
    assert int(results.split(" ")[-1]) == -1  # show in inspect
    dlg.child_window(auto_id=auto_ids_dict["close"]).click()
    dlg.wait_not("visible")

