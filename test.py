import sys,time

sys.stdout.write('DirectX 11 v11.3 Patcher')

print('')

for a in range(1,2943):
    sys.stdout.write('\r {0} files pathced out of 2943.'.format(a))
    time.sleep(0.005)

print('')
print('')
sys.stdout.write('Installing...')
print('')
sys.stdout.write('\r#####                     (33%)')
time.sleep(4)
sys.stdout.write('\r#############             (66%)')
time.sleep(7)
sys.stdout.write('\r#######################   (100%)')
print('')
print('')
sys.stdout.write('Drivers Installed, Patch Complete')
time.sleep(5)
