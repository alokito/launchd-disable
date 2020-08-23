import launchd
scopes = [launchd.plist.USER, launchd.plist.USER_ADMIN, launchd.plist.DAEMON_ADMIN]
for job in launchd.jobs():
    if job.label.startswith('com.apple'):
        continue
    if job.plistfilename is None or job.plistfilename.startswith('/System'):
        continue
    plist = launchd.plist.read(job.label)
    disabled = 'Disabled' in plist and plist['Disabled']
    runAtLoad = 'RunAtLoad' in plist and plist['RunAtLoad']
    if (not disabled or runAtLoad):
        print(f"{job.plistfilename}: {disabled}, {runAtLoad}")

