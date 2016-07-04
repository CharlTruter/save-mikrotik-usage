import urllib2
import MySQLdb
import os

# Connect to the database and open a cursor
db = MySQLdb.connect(os.environ['DATABASE_IP'],os.environ['DATABASE_USERNAME'],os.environ['DATABASE_PASSWORD'],os.environ['DATABASE_NAME'] )
cursor = db.cursor()

# Get the latest usage data from the mikrotik device
data = urllib2.urlopen("http://" + os.environ['MIKROTIK_IP'] + "/accounting/ip.cgi")
for line in data:
    # Can just use normal split here, since the data is seperated by a whitespace character.
    lines = line.split()

    # Prepare to insert the usage data into the database.
    print "Inserting usage from " + lines[0] + " to " + lines[1]
    cursor.execute("""INSERT INTO raw_usage (usage_time, from_ip_address, to_ip_address, packets, bytes_usage) VALUES (NOW(), %s,%s,%s,%s)""",(lines[0], lines[1], lines[3], lines[2]))

# Since autocommit is set to false by default (as per best practices), calling commit here will do the insert in bulk.
print "Inserting in bulk to database..."
try:
    db.commit()
except:
    db.rollback()
