# Performance Tuner

A comprehensive Python-based PC performance optimizer and system tweaker designed to maximize gaming performance, improve network connectivity, and optimize system resources.

## Features

✨ **System Optimization**
- RAM cleanup and memory optimization
- Disk cleanup and temporary file removal
- CPU performance tuning
- Startup program management
- Background service optimization

🌐 **Network Optimization**
- DNS optimization
- Network adapter tuning
- Ping and latency reduction
- Connection stability improvements
- Network cache optimization

🎮 **Gaming Performance**
- FPS optimization settings
- Latency reduction
- Network delay minimization
- GPU memory optimization
- Game-specific tweaks

📊 **System Monitoring**
- Real-time performance metrics
- CPU, RAM, and disk usage tracking
- Network latency monitoring
- FPS counter
- Ping monitoring

## Installation

### Requirements
- Windows 10/11
- Python 3.8 or higher
- Administrator privileges

### Setup

1. Clone the repository:
```bash
git clone https://github.com/bbjjk2417-lab/performance-tuner.git
cd performance-tuner
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run with administrator privileges:
```bash
python main.py
```

## Usage

```bash
# Run the main optimizer
python main.py

# Monitor system performance
python monitor.py

# Network optimization only
python network_optimizer.py

# Disk cleanup
python disk_cleaner.py
```

## Project Structure

```
performance-tuner/
├── main.py                 # Main entry point
├── monitor.py              # System monitoring
├── network_optimizer.py     # Network tuning
├── disk_cleaner.py         # Disk cleanup
├── system_optimizer.py     # System tweaks
├── gaming_optimizer.py     # Gaming-specific optimizations
├── config/                 # Configuration files
├── utils/                  # Utility functions
└── requirements.txt        # Python dependencies
```

## Features Explained

### Gaming Optimizer
Specifically optimized for Fortnite and other competitive games:
- Reduces input lag
- Optimizes GPU settings
- Frees up RAM for gaming
- Disables unnecessary processes
- Improves FPS consistency
- Reduces network delay

### Network Optimizer
Improves ping and latency:
- Optimizes DNS (uses faster servers)
- Adjusts network buffer sizes
- Reduces packet loss
- Prioritizes gaming traffic
- Disables network bandwidth limiters

### Disk Cleaner
Frees up storage space:
- Removes temporary files
- Clears system cache
- Removes old logs
- Empties recycle bin
- Removes duplicate files

### System Optimizer
Boosts overall PC performance:
- Manages startup programs
- Disables visual effects
- Optimizes power settings
- Manages background services
- Frees up system memory

## Disclaimer

⚠️ Use at your own risk. This tool modifies system settings. 
- Create a system restore point before using
- Back up important data
- Run as Administrator
- Some changes may require a system restart

## License

MIT License
