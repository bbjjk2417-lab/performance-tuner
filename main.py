#!/usr/bin/env python3
"""
Performance Tuner - Main Entry Point (Updated with License Protection)
Now uses Majus Tweaks home page
"""

import os
import sys
import time
from colorama import Fore, Back, Style, init
from utils.admin_check import check_admin
from home import MajusTweaksHome
from system_optimizer import SystemOptimizer
from network_optimizer import NetworkOptimizer
from disk_cleaner import DiskCleaner
from monitor import SystemMonitor
from gaming_optimizer import GamingOptimizer

init(autoreset=True)

class PerformanceTuner:
    def __init__(self):
        self.system_opt = SystemOptimizer()
        self.network_opt = NetworkOptimizer()
        self.disk_clean = DiskCleaner()
        self.monitor = SystemMonitor()
        self.gaming_opt = GamingOptimizer()

    def print_header(self):
        """Print Majus Tweaks header"""
        print(Fore.CYAN + Back.BLACK + """
╔════════════════════════════════════════╗
║         ⚡ MAJUS TWEAKS ⚡            ║
║    Professional PC Optimization        ║
╚════════════════════════════════════════╝
        """)

    def print_menu(self):
        """Print main menu"""
        print(Fore.GREEN + "\n" + "="*50)
        print(Fore.YELLOW + "OPTIMIZATION DASHBOARD")
        print(Fore.GREEN + "="*50)
        print(Fore.CYAN + """
1. 🎮 Gaming Optimizer (Best for Fortnite)
2. 🌐 Network Optimizer (Reduce Ping & Delay)
3. 💾 Disk Cleaner (Free up Space)
4. ⚙️  System Optimizer (CPU & RAM Tuning)
5. 📊 System Monitor (Real-time Stats)
6. 🚀 Run All Optimizations
7. ℹ️  Information
8. ❌ Exit
        """)
        print(Fore.GREEN + "="*50)

    def gaming_mode(self):
        print(Fore.MAGENTA + "\n[*] Starting Gaming Optimizer for Fortnite...")
        time.sleep(1)
        self.gaming_opt.optimize_for_gaming()

    def network_mode(self):
        print(Fore.CYAN + "\n[*] Starting Network Optimizer...")
        time.sleep(1)
        self.network_opt.optimize_network()

    def disk_mode(self):
        print(Fore.YELLOW + "\n[*] Starting Disk Cleaner...")
        time.sleep(1)
        self.disk_clean.clean_disk()

    def system_mode(self):
        print(Fore.BLUE + "\n[*] Starting System Optimizer...")
        time.sleep(1)
        self.system_opt.optimize_system()

    def monitor_mode(self):
        print(Fore.GREEN + "\n[*] Starting System Monitor...")
        print(Fore.YELLOW + "Press Ctrl+C to exit monitor\n")
        time.sleep(1)
        try:
            self.monitor.start_monitoring()
        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] Monitor stopped by user")

    def run_all(self):
        print(Fore.MAGENTA + "\n[*] Running ALL optimizations...")
        print(Fore.YELLOW + "This will take a few minutes\n")
        
        self.gaming_opt.optimize_for_gaming()
        time.sleep(2)
        
        self.network_opt.optimize_network()
        time.sleep(2)
        
        self.disk_clean.clean_disk()
        time.sleep(2)
        
        self.system_opt.optimize_system()
        
        print(Fore.GREEN + "\n✓ All optimizations completed!")

    def show_info(self):
        print(Fore.CYAN + """
╔════════════════════════════════════════╗
║      ⚡ MAJUS TWEAKS - INFORMATION ⚡  ║
╚════════════════════════════════════════╝

📋 WHAT THIS TOOL DOES:

🎮 Gaming Optimizer:
   - Disables unnecessary background services
   - Optimizes GPU settings
   - Reduces input lag
   - Improves FPS consistency
   - Optimizes memory for gaming

🌐 Network Optimizer:
   - Optimizes DNS settings
   - Reduces network latency
   - Improves ping response
   - Disables network bandwidth limiters
   - Prioritizes gaming traffic

💾 Disk Cleaner:
   - Removes temporary files
   - Clears cache
   - Removes old logs
   - Frees up disk space

⚙️  System Optimizer:
   - Manages startup programs
   - Optimizes CPU usage
   - Frees RAM memory
   - Disables visual effects

📊 System Monitor:
   - Real-time CPU usage
   - RAM consumption
   - Disk I/O
   - Network latency (Ping)

🔐 Licensed Protection:
   - Secure activation with license keys
   - Usage tracking
   - Admin management

⚠️  IMPORTANT:
   - Run with Administrator privileges
   - Create system restore point first
   - Backup important data before use

        """)

    def main_loop(self):
        self.print_header()
        
        while True:
            self.print_menu()
            choice = input(Fore.YELLOW + "Enter your choice (1-8): ").strip()

            if choice == '1':
                self.gaming_mode()
            elif choice == '2':
                self.network_mode()
            elif choice == '3':
                self.disk_mode()
            elif choice == '4':
                self.system_mode()
            elif choice == '5':
                self.monitor_mode()
            elif choice == '6':
                self.run_all()
            elif choice == '7':
                self.show_info()
            elif choice == '8':
                print(Fore.GREEN + "\n✓ Thank you for using Majus Tweaks!")
                print(Fore.CYAN + "For best results, restart your computer.\n")
                sys.exit(0)
            else:
                print(Fore.RED + "[!] Invalid choice. Please try again.")

            input(Fore.YELLOW + "\nPress Enter to continue...")


def main():
    """Main entry point with license validation"""
    # Check admin privileges
    if not check_admin():
        print(Fore.RED + "\n❌ Majus Tweaks requires Administrator privileges!")
        print(Fore.YELLOW + "Please run this script as Administrator and try again.\n")
        sys.exit(1)

    # Show home page and validate license
    home = MajusTweaksHome()
    home.launch()
    
    # If license is valid, run the main tool
    tuner = PerformanceTuner()
    tuner.main_loop()


if __name__ == "__main__":
    main()
