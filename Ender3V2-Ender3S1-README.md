Ender3V2 :

Since December 2021, Ender3V2 arrives with different hardware from the first Ender3V2:

- Motherboard with STM32F103RET6 CPU
- Motherboard with STM32F103RCT6 CPU
- Motherboard with GD32F303RET6 CPU
- LCD Display DWIN
- DACAI LCD Display

For those who have one:

- CPU STM32F103RCT6 ->
in platformio.ini, modify:
    [platform]
    src_dir=Marlin
    boards_dir = buildroot/share/PlatformIO/boards
    default_envs=STM32F103RE_creality
by :
    [platform]
    src_dir=Marlin
    boards_dir = buildroot/share/PlatformIO/boards
    default_envs=STM32F103RC_creality

- CPU GD32F303RET6 ->
in platformio.ini, modify:
    [platform]
    src_dir=Marlin
    boards_dir = buildroot/share/PlatformIO/boards
    default_envs=STM32F103RE_creality
by :
    [platform]
    src_dir=Marlin
    boards_dir = buildroot/share/PlatformIO/boards
    default_envs=STM32F103RE_creality_maple

- LCD Display DWIN ->
    Use the DWIN Display folder (in Display firmware), following the recommendations of the README.md in the Display firmware folder to update the display.

- LCD Display DACAI ->
    Use the DACAI Display folder (in Display firmware), following the recommendations of the README.md in the Display firmware folder to update the display.


Ender3 S1:

The Ender 3 S1 come with the same DACAI LCD Display of the Ender3V2. You must use the DACAI Display folder (in Display firmware), following the recommendations of the README.md in the Display firmware folder to update the display.

IMPORTANTE Note : Since March 2022, some Ender3 S1 come with an STM32F401RCT6 CPU. At the moment, Marlin does not support this new CPU for the printer. You will have to stay on the Stock Creality firmware.

