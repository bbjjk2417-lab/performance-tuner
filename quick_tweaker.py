#!/usr/bin/env python3
"""
Quick Tweaker - Fast access to individual tweaks
One-click optimization for specific tasks
"""

import os
import sys
import time
from colorama import Fore, Back, Style, init
from utils.admin_check import check_admin
from system_optimizer import SystemOptimizer
from network_optimizer import NetworkOptimizer
from disk_cleaner import DiskCleaner
from gaming_optimizer import GamingOptimizer

init(autoreset=True)


class QuickTweaker:
    """Quick access to individual tweaks"""
    
    def __init__(self):
        self.system_opt = SystemOptimizer()
        self.network_opt = NetworkOptimizer()
        self.disk_clean = DiskCleaner()
        self.gaming_opt = GamingOptimizer()

    def clean_pc(self):
        """One-click PC cleaning"""
        print(Fore.CYAN + Back.BLACK + """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║                    🧹 CLEANING YOUR PC 🧹                ║
║                                                            ║
║                  One-Click Deep Cleaning                  ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
        """)
        
        print(Fore.YELLOW + """
Starting comprehensive PC cleaning:
        """)
        
        print(Fore.CYAN + "\n[1/4] Cleaning temporary files...")
        self.disk_clean.clean_temp_files()
        
        print(Fore.CYAN + "\n[2/4] Cleaning cache files...")
        self.disk_clean.clean_cache()
        
        print(Fore.CYAN + "\n[3/4] Cleaning log files...")
        self.disk_clean.clean_logs()
        
        print(Fore.CYAN + "\n[4/4] Emptying recycle bin...")
        self.disk_clean.empty_recycle_bin()
        
        print(Fore.GREEN + """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║              ✅ PC CLEANING COMPLETED! ✅               ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
        """)
        
        self.disk_clean.show_results()
        time.sleep(2)

    def boost_gaming(self):
        """One-click gaming boost"""
        print(Fore.CYAN + Back.BLACK + """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║                  🎮 GAMING BOOST MODE 🎮                 ║
║                                                            ║
║              Optimizing Your PC for Gaming                ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
        """)
        
        print(Fore.YELLOW + """
Activating gaming optimization:
        """)
        
        self.gaming_opt.optimize_for_gaming()
        
        print(Fore.GREEN + """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║           ✅ GAMING MODE ACTIVATED! ✅                  ║
║                                                            ║
║        Your PC is now optimized for maximum gaming       ║
║                  performance! Have fun! 🎮              ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
        """)
        time.sleep(2)

    def optimize_network(self):
        """One-click network optimization"""
        print(Fore.CYAN + Back.BLACK + """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║               🌐 NETWORK OPTIMIZATION 🌐                ║
║                                                            ║
║              Reducing Ping & Latency                      ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
        """)
        
        print(Fore.YELLOW + """
Starting network optimization:
        """)
        
        self.network_opt.optimize_network()
        
        print(Fore.GREEN + """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║         ✅ NETWORK OPTIMIZATION COMPLETE! ✅            ║
║                                                            ║
║              Your ping should be lower now!              ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
        """)
        time.sleep(2)

    def full_system_tune(self):
        """One-click full system optimization"""
        print(Fore.CYAN + Back.BLACK + """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║               ⚙️ FULL SYSTEM OPTIMIZATION ⚙️            ║
║                                                            ║
║              Complete PC Performance Tune                 ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
        """)
        
        print(Fore.YELLOW + """
Running complete system optimization suite:
        """)
        
        self.system_opt.optimize_system()
        
        print(Fore.GREEN + """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║        ✅ FULL SYSTEM OPTIMIZATION COMPLETE! ✅         ║
║                                                            ║
║              Your PC is now fully optimized!             ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
        """)
        time.sleep(2)


def display_menu():
    """Display quick tweaker menu"""
    print(Fore.CYAN + Back.BLACK + """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║               ⚡ MAJUS TWEAKS - QUICK TWEAKER ⚡          ║
║                                                            ║
║              One-Click Optimization Menu                  ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    print(Fore.GREEN + """
    SELECT A QUICK TWEAK:
    
    1. 🧹 Clean PC          - Delete temp files, cache, logs
    2. 🎮 Boost Gaming      - Optimize for maximum FPS
    3. 🌐 Optimize Network  - Reduce ping and latency
    4. ⚙️  Full System Tune  - Complete optimization
    5. ❌ Exit               - Close Majus Tweaks
    
    """ + "="*58)


def main():
    """Main entry point"""
    if not check_admin():
        print(Fore.RED + "\n❌ Majus Tweaks requires Administrator privileges!")
        print(Fore.YELLOW + "Please run this script as Administrator.\n")
        sys.exit(1)

    tweaker = QuickTweaker()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_menu()
        
        choice = input(Fore.YELLOW + "\n>>> Enter your choice (1-5): " + Fore.CYAN).strip()
        
        if choice == '1':
            tweaker.clean_pc()
        elif choice == '2':
            tweaker.boost_gaming()
        elif choice == '3':
            tweaker.optimize_network()
        elif choice == '4':
            tweaker.full_system_tune()
        elif choice == '5':
            print(Fore.GREEN + "\n✓ Thank you for using Majus Tweaks!\n")
            sys.exit(0)
        else:
            print(Fore.RED + "\n❌ Invalid choice. Please try again.\n")
            time.sleep(2)


if __name__ == "__main__":
    main()
