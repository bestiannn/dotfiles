# Dotfiles in Artix Linux with Runit

My dotfiles archives in a Artix linux with Runit lol

Start mode:

![App Screenshot](img1.png)

Tiling mode:

![App Screenshot](img2.png)

## Artix linux Installation

All the information is in the official [Artix Linux Installation Guide](https://wiki.artixlinux.org/Main/Installation).

In the live iso follow the next steps.

```bash
sudo su
```

```bash
loadkeys la-latin1
```

```bash
rfkill unblock wifi
```

```bash
connmanctl
```

In the promp of this comand write

```bash
enable wifi
connmanctl scan wifi
connmanctl services
agent on
connmanctl connect [enter the code starting in "wifi_" that is assigned to the desired ssid here]
exit
```

Set the password and get out of the promp.

At this part of the we have connected the wifi, then partition your hard drive.

## Partition Disk

```bash
cfdisk /dev/sda
```

```bash
mkfs.ext4 /dev/sda5                 #ROOT
mkfs.ext4 /dev/sda6                 #HOME
mkfs.ext4 /dev/sda1                 #EFI with Windows
mkswap /dev/sda7                    #SWAP partition
```

## Mount Partition

```bash
swapon /dev/sda7
mount /dev/sda5 /mnt
mkdir /mnt/boot
mkdir /mnt/home
mount /dev/sda6 /mnt/home
mount /dev/sda1 /mnt/boot
```

## Install packages

```bash
basestrap /mnt base base-devel runit elogind-runit linux linux-firmware
```

```bash
fstabgen -U /mnt >> /mnt/etc/fstab
artix-chroot /mnt
```

## Configure the base system

In my case I will set the zone info in Santiago

```bash
ln -sf /usr/share/zoneinfo/America/Santiago /etc/localtime
```

```bash
hwclock --systohc
```

Uncoment the lines with the languages of your preferences

```bash
pacman -S nano
nano /etc/locale.gen
```

```bash
locale-gen
```

```bash
nano /etc/locale.conf
```

```bash
export LANG="en_US.UTF-8"
```

## Boot Loader

```bash
pacman -S grub os-prober efibootmgr
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=grub
os-prober
grub-mkconfig -o /boot/grub/grub.cfg
```

## Add user

Add the user root

```bash
passwd
```

Add your user

```bash
useradd -m username
passwd username
usermod -aG wheel,video,audio,storage username
```

## Network configuration

```bash
nano /etc/hostname
PC
```

```bash
nano /etc/hosts
127.0.0.1        localhost
::1              localhost
127.0.1.1        PC.localdomain  PC
```

```bash
nano /etc/sudoers
```

Uncoment the next line

```bash
## Uncomment to allow members of group wheel to execute any command
# %wheel ALL=(ALL) ALL
```

```bash
pacman -S networkmanager networkmanager-runit
```

```bash
ln -s /etc/runit/sv/NetworkManager /etc/runit/runsvdir/default
```

Now you can reboot

```bash
exit
umount -R /mnt
reboot
```

Connect your PC to wifi

```bash
# List all available networks
nmcli device wifi list
# Connect to your network
nmcli device wifi connect YOUR_SSID password YOUR_PASSWORD
```

## Login and window manager

```bash
sudo pacman -S artix-archlinux-support
```

Add the next lines in /etc/pacman.conf

```bash
# ARCH
[extra]
Include = /etc/pacman.d/mirrorlist-arch

[community]
Include = /etc/pacman.d/mirrorlist-arch

[multilib]
Include = /etc/pacman.d/mirrorlist-arch
```

```bash
sudo pacman -S xorg lightdm lightdm-gtk-greeter qtile alacritty
```

```bash
sudo ln -s /etc/runit/sv/lightdm /run/runit/service
sudo reboot
```
