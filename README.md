 <h1 align="center">Study Time Tracker</h1>

<p align="center">
  A simple Python command-line application to track study sessions and monitor total study time.
</p>

<p align="center">
  <a href="https://github.com/baraaob/study-time-tracker/releases/latest">
    <img src="https://img.shields.io/badge/Download-Windows%20EXE-blue" alt="Download Windows EXE">
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-blue" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="MIT License">
</p>

<h2>Features</h2>

<ul>
  <li>Start and stop study sessions.</li>
  <li>Calculate session duration automatically.</li>
  <li>Track accumulated study time.</li>
  <li>Save progress locally using JSON.</li>
  <li>Reset the current session without losing accumulated study time.</li>
  <li>Confirmation prompts before important actions.</li>
</ul>

<h2>Download</h2>

<p>
  Download the latest Windows executable from the
  <a href="https://github.com/baraaob/study-time-tracker/releases/latest">Releases page</a>.
</p>

<p>No Python installation is required to run the executable.</p>

<h2>Run from Source</h2>

<p>Clone the repository:</p>

```bash
git clone https://github.com/baraaob/study-time-tracker.git
cd study-time-tracker
```

<p>Run on Windows:</p>

```bash
py study_time_tracker.py
```

<p>Run on macOS or Linux:</p>

```bash
python3 study_time_tracker.py
```

<p><strong>Requirements:</strong> Python 3.10 or later. No external packages required.</p>

<h2>Menu Options</h2>

| Option | Description |
|:---:|---|
| 1 | Start the timer |
| 2 | Stop the timer and save the session |
| 3 | Reset the current running session |
| 4 | Display total study time |
| 5 | Start a new day and clear all saved data |
| 6 | Exit the program |

<h2>Data Storage</h2>

<p>
  The application stores its data in a local <code>data.json</code> file beside the Python script.
  It stores session timestamps, accumulated study time, and the current session status.
</p>

<p>
  Your personal data is stored locally and is not included in Git commits.
</p>

<h3>Important: Data Reset</h3>

<p>
  <strong>
    Starting a New Day permanently resets ALL saved data, including your total study time and session information.
  </strong>
</p>

<p>
  The current version does not maintain a history of previous days or study sessions.
  All data from the previous day is lost when you start a new day.
</p>

<h2>License</h2>

<p>
  Distributed under the <a href="LICENSE">MIT License</a>.
</p>