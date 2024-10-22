class Disk:
    def __init__(self, total, used):
        self._total = total
        self._used = used

    @property
    def free(self):
        return self._total - self._used

    @property
    def used_perc(self):
        return self._used / self._total

    def __str__(self):
        return f"Disk[total: {self._total} Gb, used: {self._used} Gb]"

    def __eq__(self, other):
        if not isinstance(other, Disk):
            return False
        return self._total == other._total and self._used == other._used

    def __lt__(self, other):
        return self.used_perc < other.used_perc

# Exemple d'utilisation
disk1 = Disk(total=10, used=2)
disk2 = Disk(total=20, used=5)

print(disk1.free)  # 8
print(disk2.free)  # 15
print(disk1.used_perc)  # 0.2
print(disk2.used_perc)  # 0.25

disks = [disk1, disk2]

 # trié selon le pourcentage d'espace utilisé
disks_sorted = sorted(disks)

for disk in disks_sorted:
    print(disk)
