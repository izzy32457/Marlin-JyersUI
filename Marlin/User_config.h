/**
 * Marlin 3D Printer Firmware
 * Copyright (c) 2020 MarlinFirmware [https://github.com/MarlinFirmware/Marlin]
 *
 * Based on Sprinter and grbl.
 * Copyright (c) 2011 Camiel Gubbels / Erik van der Zalm
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 *
 */
#pragma once

/**
 * User_Config.h
 *
 * Basic settings such as:
 *
 * - 
 *
 * Advanced settings can be found in Configuration_adv.h
 */

#if Ext_Config_JyersUI

//===========================================================================
//===========================================================================
//
// **********************  LCD and COLOR UI SETTINGS   **********************
//
//===========================================================================
//===========================================================================

// *********************  LCD DISPLAY TYPE SETTINGS  ************************
/**
 * LCD DISPLAY TYPE :
 * With this firmware, you can use 3 types of LCD Display :
 * - DWIN Display -> Stock Ender3V2 display (printers sold since their launch and
 *                   until December 2022 (subject to change)).
 * - DACAI Display -> New Ender3V2 / Ender3S1 display (printers sold since December 2021 (subject to change)).
 * - AQUILA Display -> LCD Display (sold by Voxelab) - 100% Compatible with DWIN Display.
 * 
 * If you haven't a DWIN Display, uncomment your type #define DACAI_DISPLAY 
 *    or #define AQUILA_DISPLAY (in this case, only if you have a Voxelab Aquila Printer!)
 */

//#define DACAI_DISPLAY
//#define AQUILA_DISPLAY


 /** 
  *    Shortcut Defaults
  *    0: Preheat -> Preheat menu
  *    1: Coold. -> Cooldown action
  *    2: D. Step -> Disable Steps motors
  *    3: HomeXYZ -> AutoHome
  *    4: ZOffset -> Z-Offset menu
  *    5: M.Tram. -> Manual Tramming menu
  *    6: Chg Fil -> Changement Filament
  *    7: Move Z -> Moze Live Z action
  *    8: ScreenL -> ScreenLock action
  *    9: Save -> Store Settings
  */

#define Def_Shortcut_0    0
#define Def_Shortcut_1    3


/**
 * Color list number :
 * Default(0), White(1), Light_White(2), Blue(3), Yellow(4), Orange(5), Red(6), Light_Red(7), Green(8), Light_Green(9), Magenta(10), Light_Magenta(11), Cyan(12), Light_Cyan(13), Brown(14), Black(15)
 * 
 */


  #define Def_cursor_color               5
  #define Def_menu_split_line            8
  #define Def_items_menu_text            8
  #define Def_icons_menu_text            8
  #define Def_background                 15
  #define Def_menu_top_bg                8
  #define Def_menu_top_txt               3
  #define Def_select_txt                 3
  #define Def_select_bg                  9
  #define Def_highlight_box              8
  #define Def_popup_highlight            5
  #define Def_popup_txt                  8
  #define Def_popup_bg                   15
  #define Def_ico_confirm_txt            8
  #define Def_ico_confirm_bg             15
  #define Def_ico_cancel_txt             6
  #define Def_ico_cancel_bg              15
  #define Def_ico_continue_txt           8
  #define Def_ico_continue_bg            15
  #define Def_print_screen_txt           8
  #define Def_print_filename             5
  #define Def_progress_bar               8
  #define Def_progress_percent           8
  #define Def_remain_time                8
  #define Def_elapsed_time               8
  #define Def_status_bar_text            8
  #define Def_status_area_text           8
  #define Def_status_area_percent        8
  #define Def_coordinates_text           8
  #define Def_coordinates_split_line     8



  #endif // End User_config.h