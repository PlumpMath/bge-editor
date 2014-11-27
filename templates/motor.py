# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# BGEE_Component (Mandatory for bgee catch)

# Motor.py

import GmTypes

# BeginBgeeProperties
velocity = GmTypes.GmFloat(0.1)
angularVelocity = GmTypes.GmFloat(0.01)
name = GmTypes.GmString("motor")
lives = GmTypes.GmInteger(3)
proyectile = GmTypes.GmString("proyectile")
shotVelocity = GmTypes.GmFloat(0.5)
# EndBgeeProperties

import bge
import bpy

#BeginSensors
left = "KeyboardLeftSensor"
right = "KeyboardRightSensor"
up = "KeyboardUpSensor"
down = "KeyboardDownSensor"
fire1 = "KeyboardFire1Sensor"
jump = "KeyboardJumpSensor"
#EndSensors

