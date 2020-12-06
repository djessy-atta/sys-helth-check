#!/usr/bin/env python3

import psutil
import emails
import socket


class sys_helth():
    def __init__(self, cpu_limit, disk_limit, memory_limit, localhost=('127.0.0.1', 8000)):
        self.cpu_limit = cpu_limit
        self.disk_limit = disk_limit
        self.memory_limit = memory_limit
        self.localhost = localhost

    def available_localhost(self):
        '''Check if a localhost is available'''

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind(self.localhost)
            result = True
        except:
            result = False
        sock.close()

        return result

    def check_cpu_usage_limit(self):
        '''
        Check if the cpu usage as not exceeded the limit in parameter.
        The limit in parameter should be in %
        '''
        # Get the average of the cpu usage of the last past seconde
        cpu_usage = float(psutil.cpu_percent(1))
        if cpu_usage > self.cpu_limit:
            # Return the bool true if the limit is exceeded
            return True
        else:
            # False if not
            return False

    def check_disk_space_limit(self):
        """
        Check if the free disck space as not exceeded the limit in parameter.
        The limit in parameter should be in %
        """
        # Get the available disk space in percent
        disk_space = float(psutil.disk_usage('/').total / psutil.disk_usage('/').used)
        if disk_space > self.disk_limit:
            return True
        else:
            return False

    def check_virtual_memory_limit(self):
        """
        Check if the virtual memory as not exceeded the limit in parameter.
        The limit in parameter should be in %
        """
        memory_available = (psutil.virtual_memory().used / 1000000000)
        if memory_available > self.memory_limit:
            return True
        else:
            return False


def main():

    cpu_limit = 80
    disk_limit = 80
    memory_limit = 7.5
    available_localhost = ('127.0.0.1', 8000)
    # Add the the parameter system limit to check
    sys_helth = sys_helth(cpu_limit, disk_limit, memory_limit, available_localhost)


   sender = 'djessyatta@live.fr'
   recipient = 'djessyatta@live.fr'


   if not sys_helth.available_localhost():
       # Create the subject of the message
       alert_message = "Error - localhost cannot be resolved to {}:{}".format(available_localhost[0], available_localhost[1])
       # Create the message to send
       message = emails.generate_email(sender=sender, recipient=recipient, subject=alert_message)
       # Send the message
       emails.send_email(message)

  if sys_helth.check_cpu_usage_limit():
      alert_message = "Error - CPU usage is over {}%".format(cpu_limit)
      # Create the message to send
      message = emails.generate_email(sender=sender, recipient=recipient, subject=alert_message)
      # Send the message
      emails.send_email(message)

  if sys_helth.check_disk_space_limit():
      alert_message = "Error - Available disk space is less than {}%".format(disk_limit)
      # Create the message to send
      message = emails.generate_email(sender=sender, recipient=recipient, subject=alert_message)
      # Send the message
      emails.send_email(message)

  if sys_helth.check_virtual_memory_limit():
      alert_message = "Error - Available memory is less than {}Gb".format(memory_limit)
      # Create the message to send
      message = emails.generate_email(sender=sender, recipient=recipient, subject=alert_message)
      # Send the message
      emails.send_email(message)


if __name__ == "__main__":
    main()
