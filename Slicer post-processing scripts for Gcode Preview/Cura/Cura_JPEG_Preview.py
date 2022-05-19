# By Lchristophe68 - contains some codes from Cura thumbnails plugin
# For Cura 4.x.x and Cura 5.x
import base64

from UM.Logger import Logger
from cura.Snapshot import Snapshot
from cura.CuraVersion import CuraVersion

from ..Script import Script


class Cura_JPEG_Preview(Script):
    def __init__(self):
        super().__init__()

    def _createSnapshot(self, width, height):
        Logger.log("d", "Creating thumbnail image...")
        try:
            return Snapshot.snapshot(width, height)
        except Exception:
            Logger.logException("w", "Failed to create snapshot image")

    def _encodeSnapshot(self, snapshot, quality):
        Logger.log("d", "Encoding thumbnail image...")
        try:
            thumbnail_buffer = QBuffer()
            thumbnail_buffer.open(QBuffer.ReadWrite)
            thumbnail_image = snapshot
            thumbnail_image.save(thumbnail_buffer, "JPG", quality)
            base64_bytes = base64.b64encode(thumbnail_buffer.data())
            base64_message = base64_bytes.decode('ascii')
            thumbnail_buffer.close()
            return base64_message
        except Exception:
            Logger.logException("w", "Failed to encode snapshot image")
    
    def _encodeSnapshot_v5(self, snapshot):
        Logger.log("d", "Encoding thumbnail image...")
        try:
            thumbnail_buffer = QBuffer()
            thumbnail_buffer.open(QBuffer.OpenModeFlag.ReadWrite)
            thumbnail_image = snapshot
            thumbnail_image.save(thumbnail_buffer, "JPG")
            base64_bytes = base64.b64encode(thumbnail_buffer.data())
            base64_message = base64_bytes.decode('ascii')
            thumbnail_buffer.close()
            return base64_message
        except Exception:
            Logger.logException("w", "Failed to encode snapshot image")

    def _convertSnapshotToGcode(self, encoded_snapshot, width, height, chunk_size=78):
        gcode = []

        encoded_snapshot_length = len(encoded_snapshot)
        gcode.append(";")
        gcode.append("; jpeg thumbnail begin {}x{} {}".format(
            width, height, encoded_snapshot_length))

        chunks = ["; {}".format(encoded_snapshot[i:i+chunk_size])
                  for i in range(0, len(encoded_snapshot), chunk_size)]
        gcode.extend(chunks)

        gcode.append("; thumbnail end")
        gcode.append(";")
        gcode.append("")

        return gcode

    def getSettingDataString(self):
        return """{
            "name": "Create JPEG Preview",
            "key": "Cura_JPEG_Preview",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "create_thumbnail":
                {
                    "label": "Create thumbnail",
                    "description":"Add a small thumbnail for the file selector",
                    "type": "bool",
                    "default_value": true
                },
                "create_preview":
                {
                    "label": "Create preview",
                    "description":"Add a preview image shown before printing",
                    "type": "bool",
                    "default_value": true
                }
            }
        }"""

    def execute(self, data):
    
        Major=0
        Minor=0
        try:
          Major = int(CuraVersion.split(".")[0])
          Minor = int(CuraVersion.split(".")[1])
        except:
          pass
        
        if Major < 5 :
          from PyQt5.QtCore import QByteArray, QIODevice, QBuffer
        else :
          from PyQt6.QtCore import QByteArray, QIODevice, QBuffer
        
        thumbnail_width = 50
        thumbnail_height = 50
        preview_width = 180
        preview_height = 180

        preview = self._createSnapshot(preview_width, preview_height)
        if preview and self.getSettingValueByKey("create_preview"):
            if Major < 5 :
              encoded_preview = self._encodeSnapshot(preview, 60)
            else :
              encoded_preview = self._encodeSnapshot_v5(preview)              
            preview_gcode = self._convertSnapshotToGcode(
                encoded_preview, preview_width, preview_height)

            for layer in data:
                layer_index = data.index(layer)
                lines = data[layer_index].split("\n")
                for line in lines:
                    if line.startswith(";Generated with Cura"):
                        line_index = lines.index(line)
                        insert_index = line_index + 1
                        lines[insert_index:insert_index] = preview_gcode
                        break

                final_lines = "\n".join(lines)
                data[layer_index] = final_lines

        thumbnail = self._createSnapshot(thumbnail_width, thumbnail_height)
        if thumbnail and self.getSettingValueByKey("create_thumbnail"):
            if Major < 5 :
              encoded_thumbnail = self._encodeSnapshot(thumbnail, 80)
            else :
              encoded_thumbnail = self._encodeSnapshot_v5(thumbnail)
            thumbnail_gcode = self._convertSnapshotToGcode(
                encoded_thumbnail, thumbnail_width, thumbnail_height)

            for layer in data:
                layer_index = data.index(layer)
                lines = data[layer_index].split("\n")
                for line in lines:
                    if line.startswith(";Generated with Cura"):
                        line_index = lines.index(line)
                        insert_index = line_index + 1
                        lines[insert_index:insert_index] = thumbnail_gcode
                        break

                final_lines = "\n".join(lines)
                data[layer_index] = final_lines

        return data