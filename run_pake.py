import os
import subprocess

# Update and install dependencies
subprocess.run("sudo apt update", shell=True, check=True)
subprocess.run("sudo apt install -y libwebkit2gtk-4.0-dev build-essential curl wget file libssl-dev libgtk-3-dev libayatana-appindicator3-dev librsvg2-dev", shell=True, check=True)
subprocess.run("curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh -s -- -y", shell=True, check=True)

# Load Rust environment
os.environ["PATH"] += os.pathsep + os.path.expanduser("~/.cargo/bin")

# Install pake-cli
subprocess.run("npm install -g pake-cli", shell=True, check=True)

# Run pake to package as a Windows application
subprocess.run("pake ./index.html --name html-test --use-local-file", shell=True, check=True)
