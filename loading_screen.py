#!/usr/bin/env python3
"""
Luxurious Loading Screen - Fancy entrance animation
Shows after successful license key validation
"""

import time
import sys
from colorama import Fore, Back, Style, init

init(autoreset=True)


class LuxuriousLoader:
    """Creates fancy loading screen animations"""
    
    def __init__(self, username="User"):
        self.username = username
        self.width = 65

    def clear_screen(self):
        """Clear console"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_luxury_border_top(self):
        """Print top border"""
        print(Fore.CYAN + "✦" + "▬" * (self.width - 2) + "✦")

    def print_luxury_border_bottom(self):
        """Print bottom border"""
        print(Fore.CYAN + "✦" + "▬" * (self.width - 2) + "✦")

    def print_centered(self, text, color=Fore.WHITE):
        """Print centered text"""
        spaces = (self.width - len(text)) // 2
        print(color + " " * spaces + text)

    def loading_animation_1(self):
        """Fancy loading animation with bars"""
        self.clear_screen()
        
        print(Fore.CYAN + "\n" * 2)
        self.print_luxury_border_top()
        self.print_centered("⚡ MAJUS TWEAKS ⚡", Fore.MAGENTA + Style.BRIGHT)
        self.print_centered("Premium PC Optimization Suite", Fore.CYAN)
        self.print_luxury_border_bottom()
        
        self.print_centered(f"Welcome, {self.username}!", Fore.GREEN + Style.BRIGHT)
        print("\n")
        
        # Animated loading bars
        stages = [
            "Initializing Core Engine",
            "Loading Optimization Modules",
            "Verifying System Requirements",
            "Authenticating Premium Features",
            "Preparing Dashboard Interface",
            "Configuring Performance Profiles",
            "Finalizing System Settings"
        ]
        
        for stage in stages:
            print(Fore.YELLOW + f"  ▸ {stage}")
            for i in range(20):
                sys.stdout.write(Fore.CYAN + "█")
                sys.stdout.flush()
                time.sleep(0.03)
            print(Fore.GREEN + " ✓")
            time.sleep(0.2)
        
        print("\n")
        self.print_luxury_border_top()
        self.print_centered("✨ Loading Complete ✨", Fore.GREEN + Style.BRIGHT)
        self.print_luxury_border_bottom()
        
        time.sleep(1.5)

    def loading_animation_2(self):
        """Rotating loading animation"""
        self.clear_screen()
        
        print(Fore.CYAN + "\n" * 3)
        self.print_luxury_border_top()
        self.print_centered("⚡ MAJUS TWEAKS ⚡", Fore.MAGENTA + Style.BRIGHT)
        self.print_centered("Initializing Your Dashboard", Fore.YELLOW)
        self.print_luxury_border_bottom()
        
        print("\n")
        
        spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        
        for i in range(30):
            sys.stdout.write(Fore.MAGENTA + f"\r  {spinner[i % len(spinner)]} Loading Dashboard Interface...")
            sys.stdout.flush()
            time.sleep(0.1)
        
        print(Fore.GREEN + "\r  ✓ Dashboard Ready!                       ")
        
        time.sleep(0.5)
        
        # System info display
        print(Fore.CYAN + "\n  ╔" + "═" * 57 + "╗")
        print(Fore.CYAN + "  ║" + Fore.YELLOW + " System Status: " + Fore.GREEN + "✓ Ready" + " " * 38 + Fore.CYAN + "║")
        print(Fore.CYAN + "  ║" + Fore.YELLOW + " Premium Features: " + Fore.GREEN + "✓ Unlocked" + " " * 35 + Fore.CYAN + "║")
        print(Fore.CYAN + "  ║" + Fore.YELLOW + " Optimizations Available: " + Fore.GREEN + "6+" + " " * 30 + Fore.CYAN + "║")
        print(Fore.CYAN + "  ╚" + "═" * 57 + "╝")
        
        time.sleep(1)

    def loading_animation_3(self):
        """Elegant fade-in animation"""
        self.clear_screen()
        
        # Title animation
        title_lines = [
            "    ███╗   ███╗ █████╗      ██╗██╗   ██╗███████╗",
            "    ████╗ ████║██╔══██╗     ██║██║   ██║██╔════╝",
            "    ██╔████╔██║███████║     ██║██║   ██║███████║",
            "    ██║╚██╔╝██║██╔══██║██   ██║██║   ██║╚════██║",
            "    ██║ ╚═╝ ██║██║  ██║╚█████╔╝╚██████╔╝███████║",
            "    ╚═╝     ╚═╝╚═╝  ╚═╝ ╚════╝  ╚═════╝ ╚══════╝"
        ]
        
        print("\n" * 2)
        for line in title_lines:
            print(Fore.CYAN + line)
            time.sleep(0.15)
        
        print(Fore.GREEN + "\n" + " " * 15 + "✓ PREMIUM ACCESS GRANTED\n")
        
        # Loading stages with dots
        print(Fore.MAGENTA + "  Initializing Majus Tweaks")
        stages = ["Engine", "Modules", "Features", "Interface", "System"]
        
        for stage in stages:
            sys.stdout.write(Fore.YELLOW + f"\n  ▸ Loading {stage}.")
            sys.stdout.flush()
            for _ in range(3):
                time.sleep(0.2)
                sys.stdout.write(".")
                sys.stdout.flush()
            print(Fore.GREEN + " ✓")
        
        time.sleep(0.5)

    def loading_animation_4(self):
        """Premium luxury animation"""
        self.clear_screen()
        
        print("\n" * 2)
        
        # Top decoration
        print(Fore.CYAN + "  " + "✦" * 30)
        print(Fore.CYAN + "  " + " " * 28)
        
        # Welcome message
        self.print_centered("⚡ WELCOME TO MAJUS TWEAKS ⚡", Fore.MAGENTA + Style.BRIGHT)
        self.print_centered("Premium PC Optimization Suite", Fore.CYAN)
        
        print(Fore.CYAN + "  " + " " * 28)
        
        # User greeting
        print(Fore.GREEN + "\n  " + "▸ " * 20)
        self.print_centered(f"Greetings, {self.username}!", Fore.GREEN + Style.BRIGHT)
        print(Fore.GREEN + "  " + "▸ " * 20)
        
        time.sleep(0.5)
        
        # Loading progress
        print(Fore.YELLOW + "\n  Initializing Premium Features:\n")
        
        features = [
            ("Gaming Optimizer", "🎮"),
            ("Network Tuner", "🌐"),
            ("Disk Cleaner", "💾"),
            ("System Optimizer", "⚙️"),
            ("Performance Monitor", "📊")
        ]
        
        for feature, emoji in features:
            print(Fore.CYAN + f"    {emoji} {feature}")
            for i in range(15):
                sys.stdout.write(Fore.MAGENTA + "█")
                sys.stdout.flush()
                time.sleep(0.03)
            print(Fore.GREEN + " ✓")
            time.sleep(0.1)
        
        print(Fore.CYAN + "  " + " " * 28)
        print(Fore.CYAN + "  " + "✦" * 30)
        
        print(Fore.GREEN + "\n  ✨ Dashboard Ready! Launching Interface... ✨\n")
        
        time.sleep(1.5)

    def show_random_luxury_loading(self):
        """Show one of the luxury animations"""
        import random
        animations = [
            self.loading_animation_1,
            self.loading_animation_2,
            self.loading_animation_3,
            self.loading_animation_4
        ]
        
        animation = random.choice(animations)
        animation()

    def show_module_loading(self, module_name):
        """Show loading for specific module"""
        self.clear_screen()
        
        print(Fore.CYAN + "\n" * 2)
        self.print_luxury_border_top()
        self.print_centered(f"⚡ Loading {module_name} ⚡", Fore.MAGENTA + Style.BRIGHT)
        self.print_luxury_border_bottom()
        
        print("\n")
        
        steps = [
            "Initializing module",
            "Loading optimizations",
            "Preparing interface",
            "Ready to execute"
        ]
        
        for step in steps:
            print(Fore.YELLOW + f"  ▸ {step}")
            for i in range(15):
                sys.stdout.write(Fore.CYAN + "█")
                sys.stdout.flush()
                time.sleep(0.02)
            print(Fore.GREEN + " ✓")
        
        print("\n")
        self.print_luxury_border_top()
        self.print_centered(f"✨ {module_name} Ready ✨", Fore.GREEN + Style.BRIGHT)
        self.print_luxury_border_bottom()
        
        time.sleep(1)


def show_loading_screen(username="User", animation_type=None):
    """Main function to show loading screen"""
    loader = LuxuriousLoader(username)
    
    if animation_type == "random":
        loader.show_random_luxury_loading()
    elif animation_type == "module":
        loader.show_module_loading("Dashboard")
    else:
        loader.loading_animation_4()
