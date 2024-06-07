import time
import tkinter as tk
from tkinter import messagebox
import json
import os
import subprocess
import re
import tempfile

# from tkinter import messagebox
windows_apps_dir = r"C:\Program Files\WindowsApps"
launcher_exe = "gamelaunchhelper.exe"
config = {}
cwd = os.getcwd()
games_dict, games_list, dynamic_games_list = {}, [], []
gamelist_json = "./gamelist.json"
config_json = "./config.json"
sampah = "./sampahXDDDDDD"


def donlod_gamelist():
    import urllib.request
    urllib.request.urlretrieve("https://raw.githubusercontent.com/bjdko/KEKL/main/gamelist.json", gamelist_json)


# Create the main window
root = tk.Tk()
root.title("Kanjut Badag!")
root.geometry("500x300")
root.configure(background="#ACB992")
root.attributes('-topmost', True)
# Judulge
judul = tk.Label(root, text="XDDINSIDE", font=("Georgia", 24, "bold"), fg="#362706", background="#ACB992")
judul.pack(pady=5)

# input frame
input_frame = tk.Frame(root)
input_frame.configure(background="#ACB992")
input_frame.pack()

search_label = tk.Label(input_frame, text="searchge:", font=("Georgia", 12), fg="#362706", background="#ACB992")
search_label.grid(row=0, column=0)
search_entry = tk.Entry(input_frame, background="#E9E5D6", font=("Georgia", 12), width=12)
search_entry.grid(row=0, column=1, padx=(0, 75))

delay_label = tk.Label(input_frame, text="delay:", font=("Georgia", 12), fg="#362706", background="#ACB992")
delay_label.grid(row=0, column=2)
delay_entry = tk.Entry(input_frame, width=4, background="#E9E5D6", font=("Georgia", 12))
delay_entry.grid(row=0, column=3)
s_label = tk.Label(input_frame, text="s", font=("Georgia", 12), fg="#362706", background="#ACB992")
s_label.grid(row=0, column=4)

# Create and place the search results text box
game_listbox = tk.Listbox(root, height=5, width=27, background="#E9E5D6", font=("Georgia", 18), )
game_listbox.pack(pady=5)


# Create and place the buttons
button_frame = tk.Frame(root)
button_frame.configure(background="#ACB992")
button_frame.pack(pady=10)


# FIRST TIME LAUNCH CHECK TAWAR DONLOD OR NAH?
if not os.path.exists(gamelist_json) and not os.path.exists(config_json):
    first_time = messagebox.askquestion("🚨🚨FIRST TIME LAUNCH🚨🚨", "Mau download config gx?\nkalo ga, donlod pake tombol fetch")
    if first_time == "yes":
        donlod_gamelist()


def load_gamelist():
    global games_dict, games_list, dynamic_games_list
    with open(gamelist_json, "r") as f:
        games_dict = json.load(f)
        games_list = list(games_dict.keys())
    dynamic_games_list = games_list


if os.path.exists(gamelist_json):
    load_gamelist()


def load_config():
    global config
    with open(config_json, "r") as f:
        config = json.load(f)


def write_config():
    global config
    with open(config_json, "w") as f:
        json.dump(config, f)


# configgingge
if os.path.exists(config_json):
    try:
        load_config()
    except ValueError:
        config = {
            "selected_game": "",
            "delay": 30
        }
        write_config()
else:
    config = {
        "selected_game": "",
        "delay": 30
    }
    write_config()


def run_command_as_admin(command):
    # Command to run the given command as an administrator
    runas_command = f'powershell -Command "Start-Process cmd -ArgumentList \'/c {command}\' -Verb RunAs"'

    try:
        # Run the command
        result = subprocess.run(runas_command, shell=True, capture_output=True, text=True)
        # Check if the command was successful
        if result.returncode == 0:
            print("Command executed successfully")
            return True
        else:
            print("Error executing command")
            return False
    except Exception as e:
        print(f"Exception occurred: {e}")
        return None


def fetch_gamelist():

    # Oh, no... anyways
    if os.path.exists(gamelist_json):
        donlod_or_nah = messagebox.askyesnocancel("DINK DONK", f"timpa {gamelist_json}?\\\
                                                            \nbakal tetep validasi outdated game")
        if donlod_or_nah:
            donlod_gamelist()
        elif donlod_or_nah is None:
            return
    else:
        donlod_gamelist()
    load_gamelist()
    update_listbox_entry(games_list)
    if config["selected_game"]:
        game_listbox.selection_set(games_list.index(config["selected_game"]))

    temp_output_file = os.path.join(cwd, 'temp_windowsapps_list')
    _suksescek = run_command_as_admin(f"cd /d {windows_apps_dir} & dir /B /AL > {temp_output_file}")
    __maksacek = 0
    while not os.path.exists(temp_output_file):
        time.sleep(0.4)
        __maksacek += 1
        if __maksacek >= 5:
            messagebox.showerror("berkas tidak ditemukan noway", "acc admin coek")
            return
    with open(temp_output_file, "r") as wa:
        _wa_games = wa.read().splitlines()
    os.remove(temp_output_file)
    _valid_game = ["dummy"]
    for i in games_dict:
        pkg_name = games_dict[i]["package_name"]
        if not games_dict[i]["package_name"]:
            continue
        match = re.match(r'^([^_]+)', pkg_name)
        if match:
            _no_ver = match.group(0)
        else:
            _no_ver = pkg_name
        # games_dict[i]["package_name"] = "tolol"
        for wg in _wa_games:
            if wg.startswith(_no_ver):
                games_dict[i]["package_name"] = wg
                _valid_game.append(i)

    _invalid_game = list(set(list(games_dict.keys())) - set(_valid_game))
    _invalid_game_string = "\n".join(_invalid_game)
    if _invalid_game:
        invalid_popup = messagebox.askquestion("dink donk", f"ada invalid game nichhhhh:\n{_invalid_game_string}\nDELET OR NAH?")
        if invalid_popup == "yes":
            for ccd in _invalid_game:
                del games_dict[ccd]

    with open(gamelist_json, "w") as f:
        json.dump(games_dict, f, indent=2)


def launch_after():

    # time.sleep(3)
    global sampah
    os.remove(sampah)
    exit()


def launch_action():
    global sampah
    if not config["selected_game"]:
        messagebox.showwarning("DONK", "pilih game dulu")
        return
    _game_dict = games_dict[config["selected_game"]]
    _game_path = os.path.join(windows_apps_dir, _game_dict["package_name"])
    _game_launch = os.path.join(_game_path, launcher_exe)
    if not os.path.exists(_game_launch):
        messagebox.showerror("ITIL", "Game tidaklah valid!\nCoba pencet >fetch< biar nomor versinya sesuai.")
        return
    if _game_dict["executable"].endswith("exe"):
        _game_exec_name = os.path.splitext(_game_dict["executable"])[0]
    else:
        _game_exec_name = _game_dict["executable"]
    print(_game_exec_name)
    with tempfile.NamedTemporaryFile("w", suffix=".ps1", prefix="xddinside_", delete=False) as hageuy:
        powershell_template = f"""# omagawd i lost
$processName = "{_game_exec_name}"
$delay = "{delay_entry.get()}"
$gamehelper = "{_game_launch}"
Start-Process $gamehelper
echo "GUI window utama bakal ke close"
echo "biarin konsol ini kebuka"
echo "kalo mau cancel, close window ini or..."
timeout $delay /nobreak
while ($true) {{$process = Get-Process -Name $processName -ErrorAction SilentlyContinue;if($process){{break}}echo "modcheck $processName.exe";sleep 5}}
taskkill /f /im explorer.exe
while ($true) {{$process = Get-Process -Name $processName -ErrorAction SilentlyContinue;if (-not $process) {{Start-Process "explorer.exe";break}}sleep 5}}
"""
        hageuy.write(powershell_template)
        hageuy.close()
        subprocess.Popen([
            "powershell",
            "-Command",
            f"Start-Process powershell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File \"{hageuy.name}\"'"
        ])
        sampah = hageuy.name
    search_entry.configure(state=tk.DISABLED)
    fetch_button.configure(state=tk.DISABLED)
    launch_button.configure(state=tk.DISABLED)
    exit_button.configure(state=tk.DISABLED)
    game_listbox.configure(state=tk.DISABLED)
    delay_entry.configure(state=tk.DISABLED)
    root.after(3000, launch_after)


def exit_action():
    exit()


def update_listbox_entry(data):
    game_listbox.delete(0, tk.END)
    for i in data:
        game_listbox.insert(tk.END, i)


def listbox_to_searchbox(_):
    global config, dynamic_games_list
    try:
        indexge = _.widget.curselection()[0]
        search_entry.delete(0, tk.END)
        selected_game = dynamic_games_list[indexge]
        search_entry.insert(0, selected_game)
        config["selected_game"] = selected_game
        write_config()
    except IndexError:
        pass


def realtime_search(_):
    global dynamic_games_list
    typed = search_entry.get()
    if not typed:
        data = games_list
    else:
        data = []
        for item in games_list:
            if typed.lower() in item.lower():
                data.append(item)
    dynamic_games_list = data
    update_listbox_entry(data)


def delay_check(_):
    typed = delay_entry.get()
    try:
        typed = int(typed)
    except ValueError:
        typed = 0
    config["delay"] = max(0, typed)
    write_config()


fetch_button = tk.Button(button_frame, text="fetch", command=fetch_gamelist, bg="#464E2E", fg="#E9E5D6",
                         font=("Georgia", 8, "bold"), width=5)
fetch_button.grid(row=0, column=0, padx=5)

launch_button = tk.Button(button_frame, text="launch", command=launch_action, bg="#464E2E", fg="#E9E5D6",
                          font=("Georgia", 8, "bold"), width=8)

launch_button.grid(row=0, column=1, padx=5)

exit_button = tk.Button(button_frame, text="exit", command=exit_action, bg="#464E2E", fg="#E9E5D6",
                        font=("Georgia", 8, "bold"), width=5)
exit_button.grid(row=0, column=2, padx=5)

# scriptge
update_listbox_entry(games_list)
search_entry.insert(tk.END, config["selected_game"])
if config["selected_game"] in games_list:
    game_listbox.selection_set(games_list.index(config["selected_game"]))
if config["delay"]:
    delay_entry.insert(tk.END, config["delay"])
game_listbox.bind("<<ListboxSelect>>", listbox_to_searchbox)
search_entry.bind("<KeyRelease>", realtime_search)
delay_entry.bind("<KeyRelease>", delay_check)

# Run the application
root.mainloop()
