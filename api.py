#!/usr/bin/env python3
import wifi_qrcode_generator.generator

qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
    ssid='vanVosbergen_Gast', hidden=False, authentication_type='WPA', password='1701AR20Heerhugowaard'
)
qr_code.print_ascii()
qr_code.make_image().save('vanVosbergen_Gast.png')