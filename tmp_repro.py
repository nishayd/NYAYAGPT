import sys
sys.path.insert(0, 'd:/NYAYAGPT')
try:
    import app
    print('app imported successfully')
except Exception:
    import traceback
    traceback.print_exc()
