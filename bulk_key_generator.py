#!/usr/bin/env python3
"""
Bulk License Key Generator - Create 1000 keys with different durations
Mix of lifetime, 30-day, and 7-day keys
"""

import json
import os
import secrets
from datetime import datetime, timedelta
from colorama import Fore, Back, Style, init

init(autoreset=True)


class BulkKeyGenerator:
    def __init__(self, keys_file="licenses/license_keys.json"):
        self.keys_file = keys_file
        self.ensure_directory()
        self.keys = {}

    def ensure_directory(self):
        """Create licenses directory if it doesn't exist"""
        os.makedirs("licenses", exist_ok=True)

    def load_existing_keys(self):
        """Load any existing keys"""
        if os.path.exists(self.keys_file):
            try:
                with open(self.keys_file, 'r') as f:
                    self.keys = json.load(f)
                    return len(self.keys)
            except:
                self.keys = {}
        return 0

    def generate_bulk_keys(self, count=1000):
        """Generate bulk keys with mixed durations"""
        print(Fore.CYAN + Back.BLACK + """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║           BULK LICENSE KEY GENERATOR                       ║
║                                                            ║
║        Creating 1000 Premium Keys for Majus Tweaks        ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
        """)
        
        existing = self.load_existing_keys()
        
        if existing > 0:
            print(Fore.YELLOW + f"\n⚠️  Found {existing} existing keys!")
            choice = input(Fore.CYAN + "\nClear and regenerate? (Y/N): ").strip().upper()
            if choice != 'Y':
                print(Fore.YELLOW + "Keeping existing keys...")
                return existing
            self.keys = {}
        
        # Distribution: 250 lifetime, 400 30-day, 350 7-day
        distributions = [
            ("lifetime", 250, None),
            ("30days", 400, 30),
            ("7days", 350, 7)
        ]
        
        total_generated = 0
        
        for key_type, amount, days in distributions:
            print(Fore.MAGENTA + f"\n{'='*60}")
            print(Fore.YELLOW + f"Generating {amount} {key_type.upper()} Keys...")
            print(Fore.MAGENTA + f"{'='*60}\n")
            
            for i in range(amount):
                key = self.generate_single_key()
                
                if days is None:
                    expiry = (datetime.now() + timedelta(days=36500)).isoformat()  # ~100 years
                    expiry_text = "LIFETIME"
                else:
                    expiry = (datetime.now() + timedelta(days=days)).isoformat()
                    expiry_text = f"{days} DAYS"
                
                # Create realistic usernames
                usernames = [
                    f"gamer_{i}", f"player_{i}", f"fortnite_{i}",
                    f"streamer_{i}", f"pro_{i}", f"legend_{i}",
                    f"tryhard_{i}", f"noob_{i}", f"veteran_{i}",
                    f"speedrunner_{i}", f"content_{i}", f"team_{i}"
                ]
                
                username = usernames[i % len(usernames)]
                
                self.keys[key] = {
                    "username": username,
                    "created": datetime.now().isoformat(),
                    "expires": expiry,
                    "active": True,
                    "type": "ULTIMATE",
                    "duration": key_type,
                    "usage_count": 0,
                    "last_used": None
                }
                
                total_generated += 1
                
                # Progress bar
                progress = (i + 1) / amount
                bar_length = 50
                filled = int(bar_length * progress)
                bar = "█" * filled + "░" * (bar_length - filled)
                
                print(Fore.CYAN + f"\r  [{bar}] {i + 1}/{amount} Keys Generated", end="", flush=True)
            
            print(Fore.GREEN + f" ✓ DONE!\n")
        
        # Save all keys
        print(Fore.MAGENTA + f"{'='*60}")
        print(Fore.YELLOW + "Saving all keys to file...")
        print(Fore.MAGENTA + f"{'='*60}\n")
        
        with open(self.keys_file, 'w') as f:
            json.dump(self.keys, f, indent=2)
        
        print(Fore.GREEN + f"✅ Successfully generated {total_generated} license keys!\n")
        
        return total_generated

    def generate_single_key(self):
        """Generate a single license key"""
        random_part = secrets.token_hex(8).upper()
        key = f"MAJUS-{random_part[:4]}-{random_part[4:8]}-{random_part[8:16]}"
        return key

    def export_keys_to_file(self):
        """Export keys in text format for easy sharing"""
        print(Fore.CYAN + "\nExporting keys to text file...")
        
        with open("licenses/LICENSE_KEYS_LIST.txt", "w") as f:
            f.write("="*70 + "\n")
            f.write("MAJUS TWEAKS - LICENSE KEYS\n")
            f.write("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            f.write("="*70 + "\n\n")
            
            lifetime_keys = []
            thirty_day_keys = []
            seven_day_keys = []
            
            for key, info in self.keys.items():
                if info['duration'] == 'lifetime':
                    lifetime_keys.append(key)
                elif info['duration'] == '30days':
                    thirty_day_keys.append(key)
                else:
                    seven_day_keys.append(key)
            
            f.write(f"LIFETIME KEYS ({len(lifetime_keys)}):\n")
            f.write("-" * 70 + "\n")
            for i, key in enumerate(lifetime_keys, 1):
                f.write(f"{i:3d}. {key}\n")
            
            f.write(f"\n\n30-DAY KEYS ({len(thirty_day_keys)}):\n")
            f.write("-" * 70 + "\n")
            for i, key in enumerate(thirty_day_keys, 1):
                f.write(f"{i:3d}. {key}\n")
            
            f.write(f"\n\n7-DAY KEYS ({len(seven_day_keys)}):\n")
            f.write("-" * 70 + "\n")
            for i, key in enumerate(seven_day_keys, 1):
                f.write(f"{i:3d}. {key}\n")
        
        print(Fore.GREEN + "✅ Keys exported to: licenses/LICENSE_KEYS_LIST.txt\n")

    def print_key_summary(self):
        """Print summary of generated keys"""
        print(Fore.CYAN + Back.BLACK + """
╔════════════════════════════════════════════════════════════╗
║                   KEY GENERATION SUMMARY                  ║
╚════════════════════════════════════════════════════════════╝
        """)
        
        lifetime = sum(1 for k in self.keys.values() if k['duration'] == 'lifetime')
        thirty = sum(1 for k in self.keys.values() if k['duration'] == '30days')
        seven = sum(1 for k in self.keys.values() if k['duration'] == '7days')
        
        print(Fore.GREEN + f"""
  📊 TOTAL KEYS GENERATED: {len(self.keys)}
  
  🌟 LIFETIME KEYS: {lifetime}
     └─ Never expire, can distribute to loyal users
     └─ Best for: Premium members, friends
  
  📅 30-DAY KEYS: {thirty}
     └─ Expire in 30 days
     └─ Best for: Trial period, event keys
  
  ⏰ 7-DAY KEYS: {seven}
     └─ Expire in 7 days
     └─ Best for: Free trial, limited access
        """)
        
        print(Fore.MAGENTA + "="*60)
        print(Fore.CYAN + "\nKey Distribution Ready! 🎉\n")
        
        print(Fore.YELLOW + """
HOW TO USE THESE KEYS:

1. SHARE LIFETIME KEYS (250)
   → Give to friends, family, loyal users
   → They get access forever
   → No expiration

2. SHARE 30-DAY KEYS (400)
   → Distribute at events, through referrals
   → Users get 1 month access
   → Then they can purchase lifetime

3. SHARE 7-DAY KEYS (350)
   → Free trial for new users
   → Let them experience Majus Tweaks
   → They'll want to upgrade to 30 or lifetime

TOTAL: 1000 KEYS for distribution! 🚀
        """)


def main():
    """Main entry point"""
    generator = BulkKeyGenerator()
    
    total = generator.generate_bulk_keys(1000)
    generator.print_key_summary()
    generator.export_keys_to_file()
    
    print(Fore.GREEN + """
✅ All done!

Next steps:
1. Find keys in: licenses/LICENSE_KEYS_LIST.txt
2. Share them with your community
3. People run: python main.py
4. They enter a key and get access!

Files created:
  • licenses/license_keys.json (1000 keys in database)
  • licenses/LICENSE_KEYS_LIST.txt (1000 keys in text format)
    """)


if __name__ == "__main__":
    main()
