#!/usr/bin/env python3
"""
Majus Tweaks - Welcome Page & License Key Entry
Beautiful home page for Performance Tuner
"""

import os
import sys
import time
from colorama import Fore, Back, Style, init
from license_validator import LicenseValidator

init(autoreset=True)

class MajusTweaksHome:
    def __init__(self):
        self.validator = LicenseValidator()

    def clear_screen(self):
        """Clear console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_logo(self):
        """Print cool Majus Tweaks logo"""
        logo = Fore.CYAN + """
    ███╗   ███╗ █████╗      ██╗██╗   ██╗███████╗
    ████╗ ████║██╔══██╗     ██║██║   ██║██╔════╝
    ██╔████╔██║███████║     ██║██║   ██║███████╗
    ██║╚██╔╝██║██╔══██║██   ██║██║   ██║╚════██║
    ██║ ╚═╝ ██║██║  ██║╚█████╔╝╚██████╔╝███████║
    ╚═╝     ╚═╝╚═╝  ╚═╝ ╚════╝  ╚═════╝ ╚══════╝
    """ + Fore.RESET
        
        return logo

    def print_home_screen(self):
        """Print beautiful home screen"""
        self.clear_screen()
        
        print(Fore.CYAN + Back.BLACK + """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║                    ⚡ MAJUS TWEAKS ⚡                   ║
║                                                           ║
║            Professional PC Optimization Suite            ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
        """)
        
        print(self.print_logo())
        
        print(Fore.YELLOW + """
    🎮 Gaming Performance  |  🌐 Network Boost  |  💾 Cleanup
    ⚙️  System Tuning     |  📊 Monitoring    |  🔐 Protected
        """)
        
        print(Fore.GREEN + """
╔═══════════════════════════════════════════════════════════╗
║                   WELCOME TO MAJUS TWEAKS                ║
║                                                           ║
║  Your PC deserves the best performance. Majus Tweaks     ║
║  delivers professional-grade optimization for gaming,    ║
║  streaming, and everyday use.                            ║
║                                                           ║
║  ✓ Licensed Protection  ✓ Premium Features               ║
║  ✓ Real-time Monitoring ✓ Expert Tuning                  ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
        """)

    def print_license_screen(self):
        """Print license key entry screen"""
        print(Fore.CYAN + Back.BLACK + """
╔═══════════════════════════════════════════════════════════╗
║                   ACTIVATE MAJUS TWEAKS                  ║
║                                                           ║
║            Enter your License Key to Continue            ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
        """)
        
        print(Fore.YELLOW + """
    📋 License Key Format: PERF-XXXX-XXXX-XXXX
    
    Don't have a license key?
    → Contact the administrator
    → Get your personalized key
        """)

    def request_license_animated(self):
        """Request license key with cool animation"""
        max_attempts = 3
        
        for attempt in range(max_attempts):
            self.print_home_screen()
            self.print_license_screen()
            
            # Animated dots
            dots = "." * ((attempt % 3) + 1) + " " * (2 - (attempt % 3))
            
            print(Fore.CYAN + f"\n    Verifying License {dots}\n")
            
            key = input(Fore.GREEN + "    🔑 Enter License Key: " + Fore.YELLOW).strip().upper()
            
            if not key:
                print(Fore.RED + "\n    ❌ License key cannot be empty!\n")
                time.sleep(2)
                continue
            
            # Validate key
            print(Fore.CYAN + "\n    🔍 Validating license key...\n")
            time.sleep(1)
            
            valid, message = self.validator.manager.validate_key(key)
            
            if valid:
                self.show_success_screen(message)
                return True
            else:
                remaining = max_attempts - attempt - 1
                self.show_error_screen(message, remaining)
                
                if remaining == 0:
                    return False
        
        return False

    def show_success_screen(self, message):
        """Show success screen"""
        self.clear_screen()
        
        print(Fore.GREEN + Back.BLACK + """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║                  ✅ LICENSE ACTIVATED! ✅               ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
        """)
        
        print(self.print_logo())
        
        print(Fore.GREEN + f"""
    {message}
    
    🎉 Welcome to Majus Tweaks Premium! 🎉
    
    Get ready to transform your PC performance.
    Loading your personalized dashboard...
        """)
        
        # Loading animation
        print(Fore.CYAN + "\n    ", end="", flush=True)
        for i in range(5):
            print("▓", end="", flush=True)
            time.sleep(0.3)
        print(" 100%\n")
        
        time.sleep(2)

    def show_error_screen(self, message, remaining):
        """Show error screen"""
        self.clear_screen()
        
        print(Fore.RED + Back.BLACK + """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║              ❌ LICENSE VALIDATION FAILED ❌             ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
        """)
        
        print(self.print_logo())
        
        if remaining > 0:
            print(Fore.YELLOW + f"""
    {message}
    
    ⚠️  Attempts remaining: {remaining}
    
    💡 Tips:
    • Make sure you copied the key correctly
    • Check for spaces at the beginning/end
    • Key format: PERF-XXXX-XXXX-XXXX
        """)
        else:
            print(Fore.RED + f"""
    {message}
    
    ❌ Maximum attempts exceeded!
    
    Access denied. Please contact the administrator
    for a valid license key.
    
    Your trial period has ended.
    """)
        
        time.sleep(2)

    def show_invalid_screen(self):
        """Show invalid/expired screen"""
        self.clear_screen()
        
        print(Fore.RED + Back.BLACK + """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║              ⛔ ACCESS DENIED - TRIAL EXPIRED ⛔         ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
        """)
        
        print(self.print_logo())
        
        print(Fore.RED + """
    Your license has expired or is invalid.
    
    To continue using Majus Tweaks:
    
    1. Contact your administrator
    2. Request a new license key
    3. Restart the application
    
    Majus Tweaks Team
    ⚡ Professional PC Optimization ⚡
        """)
        
        time.sleep(3)

    def launch(self):
        """Launch the home page and license validation"""
        while True:
            if self.request_license_animated():
                return True
            else:
                self.show_invalid_screen()
                sys.exit(1)


def main():
    """Main entry point"""
    home = MajusTweaksHome()
    home.launch()


if __name__ == "__main__":
    main()
