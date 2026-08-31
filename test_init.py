#!/usr/bin/env python
import sys
sys.path.insert(0, '.')

try:
    print("1. Importing database module...")
    import database
    print("   ✅ database imported")
    
    print("2. Importing support_logic module...")
    import support_logic
    print("   ✅ support_logic imported")
    
    print("3. Initializing database...")
    database.init_database()
    print("   ✅ database initialized")
    
    print("4. Querying tickets...")
    conn = database.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as count FROM tickets")
    count = cursor.fetchone()['count']
    print(f"   ✅ Found {count} tickets in database")
    conn.close()
    
    print("\n✅ ALL TESTS PASSED!")
    
except Exception as e:
    print(f"\n❌ ERROR: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
