#!/bin/bash


# the following tests are for sites x1 and x2 prod environments

# for prod env we schedule downtime in datadog.
# the down time script needs to be run for each env seperately

echo "hello dev/test"
./schedule_downtime.sh x1
./schedule_downtime.sh x2

# edit the yaml file before running the ansibel script
# for prod group1 mke the hosts point to grp1_prod

sed -i 's/\(hosts: \).*/\1grp2_prd/' ../files/test_ansible.yml
echo " the new value of ansible playbook hosts is $( grep hosts ../files/test_ansible.yml) "
