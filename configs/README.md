# ESP32 S3 WROOM-1 N16R8 16MB PSRAM 8MB Pinout:

<div align="center">
  <img src="../../docs/ESP32-S3-16MB-PSRAM-8MB.png" alt="ESP32 S3 WROOM-1 N16R8 16MB FLASH PSRAM 8MB">
</div>

<div align="center">
  <ul>
    <a href="../../docs/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf" target="_blank">ESP32 S3 WROOM-1 Datasheet</a>
    <br>
    <a href="https://documentation.espressif.com/esp-dev-kits/en/latest/esp32s3/esp32-s3-devkitc-1/user_guide_v1.1.html" target="_blank">ESP32 S3 WROOM-1 Docs</a>
  </ul>
</div>

----

- SPI principal (`FSPI`) - `SPI_ID=1`

----

| Nombre normal |	Nombre en tabla	| Pin J3 (No.)	| Pin Name |
|---------------|-----------------|---------------|----------|
| CS            |	FSPICS0	        | 16	          | GPIO 10  |
| SDA	          | FSPID/MOSI      | 17	          | GPIO 11  |
| SCL   	      | FSPICLK	        | 18	          | GPIO 12  |
| SDO           |	FSPIQ/MISO      | NC	          | None     |

----

# Displays Modules

The following folders contain `tft_config.py` modules used by the example programs to configure the display. Install the appropiate configuration module for your device.

Folder          | Device
--------------- | ------------------------------------------------------------------
esp32s3-N16R8   | ESP32 S3 WROOM-1 N16R8 st7789 1.9" IPS RGB Module 170x320 Display

# 1,9" IPS Module SPI 170x320 (RGB) Pinout:

| Nombre normal |	Nombre en tabla	| Pin J3 & J1 (No.)	| Pin Name |
|---------------|-----------------|-------------------|----------|
| GND           | GND             | 44                | GND      |
| VCC           | 3V3             |  1                | 3V3      |
| SCL           | FSPICLK         | 18                | GPIO 12  |
| SDA           | FSPID/MOSI      | 17	              | GPIO 11  |
| RES           | --------------- |  7                | GPIO  7  |
| DC            | --------------- |  6                | GPIO  6  |
| CS            | FSPICS0	        | 16	              | GPIO 10  |
| BLK           | --------------- |  2                | GPIO  4  |

----

# Button Modules

These following folders contain `buttons.py` config modules that are used by the `roids.py` example program to configure the buttons.

Folder          | Device
--------------- | ------------------------------------------------------------------
esp32s3-N16R8   | ESP32 S3 WROOM-1 N16R8 st7789 1.9" IPS RGB Module 170x320 Display

# TFT_BUTTONS Pinout:
- Name: `esp32s3-n16r8`

| Nombre normal | Pin J3 & J1 (No.)	| Pin Name |
|---------------|-------------------|----------|
| left          |  8                | GPIO 15  |
| right         |  9                | GPIO 16  |
| hyper         | 10                | GPIO 17  |
| thrust        | 11	              | GPIO 18  |
| fire          | 27                | GPIO 21  |

----

<div align="center">
  <table>
    <tr>
      <td>
        <a href="../../docs/ESP32-S3_DevKitC-1_pinlayout_v1.1.jpg" target="_blank">
          <img src="../../docs/ESP32-S3_DevKitC-1_pinlayout_v1.1.jpg" width="100%">
        </a>
      </td>
      <td>
        <a href="../../docs/MSP1901.png" target="_blank">
          <img src="../../docs/MSP1901.png" width="100%">
        </a>
      </td>
    </tr>
  </table>
</div>

----

<h3>ESP32 S3 WROOM-1 Datasheet:</h3>

----

<div align="left">
    <a href="../../docs/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf" target="_blank">
      <img src="../../docs/esp32-s3-wroom-1_wroom-1u_datasheet_en.webp" width="40%">
    </a>
</div>

----

<h3>ESP32 S3 Series Datasheet:</h3>

----

<div align="left">
    <a href="../../docs/esp32-s3_Series_datasheet_en.pdf" target="_blank">
      <img src="../../docs/esp32-s3_Series_datasheet_en.webp" width="40%">
    </a>
</div>

----

<h3>ESP32 S3 Technical Reference Manual:</h3>

----

<div align="left">
    <a href="../../docs/esp32-s3_technical_reference_manual_en.pdf" target="_blank">
      <img src="../../docs/esp32-s3_technical_reference_manual_en.webp" width="40%">
    </a>
</div>

----

<h3>ESP32 S3 Hardware Design Guidelines:</h3>

----

<div align="left">
    <a href="../../docs/esp-hardware-design-guidelines-en-master-esp32s3.pdf" target="_blank">
      <img src="../../docs/esp-hardware-design-guidelines-en-master-esp32s3.webp" width="40%">
    </a>
</div>

----
