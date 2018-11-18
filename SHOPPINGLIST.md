﻿# Shopping List

All components were sourced in Sydney, Australia through 2018. We won't anticipate you'll have any problems sourcing these items.

## Photographic
* #### A camera (Canon 60D)
See the "Engineering Decisions" page for the logic behind specifying this.

eBay
    
    $AUD400

* #### 18-55mm EF-S Lens

See the "Engineering Decisions" page for the logic behind specifying this.
eBay
    
    $AUD75

* #### DC  Power Coupler to suit

Aka a "fake battery". We cut off the USB plugs and soldered the cable directly to the PCB. If your camera has an auxiliary power input this won't be necessary. Substitute a suitable plug and cable.

<a href="https://www.ebay.com/itm/Power-bank-usb-for-Canon-EOS-5D-7D-Mark-II-6D-80D-camera-DR-E6-dc-coupler-LP-E6/123101336453?hash=item1ca9695385:g:dWAAAOSwsQFa4ZVV:rk:1:pf:0" target="_blank">eBay</a>
    
$USD25, ~$AUD35

* #### Shutter Release cable to suit

PhotoShopStudio
    
$10

* #### 77-82mm filter step-up ring

PhotoShopStudio
    
$10	

* #### 82mm UV (or ND) filter

PhotoShopStudio
    
$50

* #### Right-Angle Mini-B USB cable

This one's optional, and depends on your choice of housing and camera. We wanted a right-angle USB plug to come out of the camera. This one ended in a Male A, necessitating the use of the second USB cable (see Electronics/ Pi).

<a href="https://www.ebay.com.au/itm/112701227087" target="_blank">eBay</a>

$AUD2


### SUBTOTAL: $582

## Power

* #### 12V Sealed Lead-Acid Battery
Careful with this one. The battery we went with only *just* fits inside the Pelican case.

12V 2.2Ah SLA Battery

<a href="https://www.jaycar.com.au/12v-2-2ah-sla-battery/p/SB2482" target="_blank">Jaycar Electronics (AU)</a>
    
$AUD24

* #### 12V Solar Charger

12V 6A Battery Charging Regulator for Solar Panels

<a href="https://www.jaycar.com.au/12v-6a-battery-charging-regulator-for-solar-panels/p/AA0348" target="_blank">Jaycar Electronics (AU)</a>

$AUD30

* #### 20 watt solar panel

12V 20W MONO SOLAR PANEL TRICKLE POWER CHARGER RV AGM Complete Kit 4WD 4x4

<a href="https://www.ebay.com.au/itm/112750149497" target="_blank">eBay</a>
    
$AUD49


* #### Cable entry gland

You only need two holes in the box - one to let the light in, and another for the power. For the power input, you'll need some sort of gland to provide a water-tight seal.

You should be able to source these from your nearest electrical wholesaler, hobbyist electronics shop, or maybe a marine supplies shop (if you're near water).

<a href="https://www.cabac.com.au/product-specs/13450510/GN12S" target="_blank">Cabac (AU)</a>

$AUD2 (?)

* #### Miscellaneous

Your choice of solar panel might require some bracing or a bracket in order for it to mount to a pole. For ours we used two lengths of some 2" aluminium angle that we had to hand, resulting in a U-shaped support.

$AUD ??

### SUBTOTAL: $103


##  Electronics
* #### Arduino Pro Mini 328 

I went with the 3.3V 8MHz model for its minimal current consumption and pin-compatibility with the Pi's 3.3V IO pins. You *will* get better performance out of the 5V version, but also inherit an obligation to add a level converter for the pins (not described here). 

<a href="https://www.sparkfun.com/products/11114" target="_blank">3.3V - SparkFun</a>

<a href="https://www.robotgear.com.au/Product.aspx/Details/1993-Arduino-Pro-Mini-328-3-3V-8MHzhttps://www.robotgear.com.au/Product.aspx/Details/1993-Arduino-Pro-Mini-328-3-3V-8MHz" target="_blank">3.3V - Robot Gear (Australia)</a>

$AUD16

* #### FTDI programming cable

Don't be tempted to go with a generic 5V programming cable - stick with a 3.3V version to match the Arduino, otherwise your in-situ programming will result in the Arduino presenting 5V into the 3.3V pins of the Pi.

<a href="https://www.robotgear.com.au/Product.aspx/Details/1615-SparkFun-FTDI-Basic-Breakout-3-3V" target="_blank">Robot Gear (AU)</a>

$AUD25

* #### Raspberry Pi Zero W

I went for the Pi Zero as it met my needs for a low-current, low-cost unit in a small footprint - and less than half the cost of the larger models. There's nothing stopping you upgrading to a Model 2 or 3, but be aware that some of the config options will be slightly different.

<a href="https://www.robotgear.com.au/Product.aspx/Details/5288-Raspberry-Pi-Zero-Whttps://www.robotgear.com.au/Product.aspx/Details/5288-Raspberry-Pi-Zero-W" target="_blank">Robot Gear (Australia)</a>

$AUD25

* #### USB "OTG" cable

You will recognise this as a micro-USB plug to a USB-A socket, but it's officially known as an On-The-Go (OTG) cable. Your Pi supplier probably offers these as an option with the Pi, so you can connect "standard" USB peripherals to the Pi. It's only required in the finished unit if you can't source a single USB cable to run from the camera to the Pi.

<a href="https://www.robotgear.com.au/Product.aspx/Details/5287-USB-OTG-Cable-Female-A-to-Micro-B-5in" target="_blank">Robot Gear (AU)</a>

<a href="https://core-electronics.com.au/micro-usb-otg-host-cable-for-raspberry-pi-zero.html" target="_blank">Core Electronics (AU)</a>

$AUD5

* #### Mini HDMI cable/adapter

As with the OTG cable, your Pi supplier will surely offer these with the Pi, as you'll need it to connect your desktop monitor for the initial config steps.

<a href="https://www.robotgear.com.au/Product.aspx/Details/5285-Mini-HDMI-Cable-3ft" target="_blank">Robot Gear (AU) - cable</a>

<a href="https://core-electronics.com.au/mini-hdmi-to-standard-hdmi-jack-adapter-for-raspberry-pi-zero.html" target="_blank">Core Electronics (AU) - adapter</a>

$AUD8


* #### SanDisk 128GB Ultra Micro SDXC Memory Card

Choosing a larger size allows you to maximise the off-camera storage in the Pi. Be careful though, as once you go over 32G you're beyond the capabilities of the FAT file system and you're at greater risk of finding the Pi won't read the card. I used <a href="https://elinux.org/RPi_SD_cards" target="_blank">"RPi SD cards"</a> as a helpful reference to find the card we went with here.

<a href="https://wwhttps://www.officeworks.com.au/shop/officeworks/p/sandisk-128gb-ultra-micro-sdxc-memory-card-sdsq128gbw.officeworks.com.au/shop/officeworks/p/sandisk-128gb-ultra-micro-sdxc-memory-card-sdsq128gb" target="_blank">Officeworks (AU)</a>

$AUD50


* #### Real-Time Clock
DeadOn RTC Breakout - DS3234

<a href="https://www.sparkfun.com/products/10160" target="_blank">SparkFun BOB-10160</a>

<a href="https://www.robotgear.com.au/Product.aspx/Details/1693-SparkFun-DeadOn-RTC-Breakout-DS3234https://www.robotgear.com.au/Product.aspx/Details/1693-SparkFun-DeadOn-RTC-Breakout-DS3234" target="_blank">Robot Gear (Australia)</a>

$AUD24

* #### Coin-cell Backup Battery

The DeadOn RTC requires a 3V lithium backup battery. The common CR1225 or the slightly thinner CR1220 are compatible here. Your DeadOn supplier will probably have these in stock, otherwise they're the sort of item you might get from the local electronics hobby store or key-cutting kiosk.

<a href="https://www.jaycar.com.au/cr1220-3v-lithium-battery/p/SB2527" target="_blank">CR1220 - Jaycar Electronics (AU)</a>

$AUD3

* #### 3.3V regulator (Arduino)

Pololu 3.3V, 500mA Step-Down Voltage Regulator D24V5F3

<a href="https://www.pololu.com/product/2842" target="_blank">Pololu 2842</a>

<a href="https://core-electronics.com.au/pololu-3-3v-500ma-step-down-voltage-regulator-d24v5f3.html" target="_blank">Core Electronics (AU)</a>

<a href="https://www.robotgear.com.au/Product.aspx/Details/1017-3-3V-500mA-Pololu-Step-Down-Voltage-Regulator-D24V5F3" target="_blank">Robot Gear (AU)</a>

$AUD7


* #### 5.0V regulator (Raspberry Pi)

Pololu 5V, 500mA Step-Down Voltage Regulator D24V5F5

<a href="https://www.pololu.com/product/2843" target="_blank">Pololu 2843</a>

<a href="https://core-electronics.com.au/pololu-5v-500ma-step-down-voltage-regulator-d24v5f5.html" target="_blank">Core Electronics (AU)</a>

<a href="https://www.robotgear.com.au/Product.aspx/Details/1018-5V-500mA-Pololu-Step-Down-Voltage-Regulator-D24V5F5" target="_blank">Robot Gear (AU)</a>

$AUD7

* #### 7.5V regulator (Camera)

Pololu 7.5V, 2.4A Step-Down Voltage Regulator D24V22F7

<a href="https://www.pololu.com/product/2860" target="_blank">Pololu 2860</a>

<a href="https://www.robotgear.com.au/Product.aspx/Details/1007-7-5V-2-4A-Pololu-Step-Down-Voltage-Regulator-D24V22F7" target="_blank">Robot Gear (AU)</a>

$AUD13

* #### Opto-Isolators

I went with bog-standard Motorola 4N25 6-pin DIP opto-isolators. These (or an equivalent) should be easy enough to find anywhere.

<a href="https://au.element14.com/vishay/4n25/optocoupler-transistor-5300vrms/dp/1612453?st=4n25" target="_blank">Element 14</a>

$AUD1 (each - you need two)

* ### Concealed Timber Door Frame Reed Switch
So as to save opening the case when its in situ, we added a standard door reed switch you might find used in a burglar alarm. Wave a magnet on the outside of the box, and in the configuration presented here it will wake the Raspberry Pi for the previously-set "WakeTime" duration. (Again, this presumes a low-power setup with the Pi normally turned off).

<a href="https://www.jaycar.com.au/concealed-timber-door-frame-reed-switch/p/LA5075" target="_blank">Jaycar (AU)</a>

$AUD5


* #### 2.5mm stereo socket

This is to connect the intervalm8r to the camera's shutter cable. I went with a though-hole plate-mounted version here, but you could just as easily choose PCM mount or in-line instead. Change this to a suitable connector if your camera shutter release cable has a differnt connector.

* #### 3mm Green LED (optional)

As the project is presented, this LED lights when the Arduino is awake, but only if the adjacent jumper is connected (taking Arduino input A0 to ground). I used it as a generic headless debugging aid. You should be able to find this just about anywhere: your Arduino/Pi supplier, local electronics hobby store, etc.

$AUD1

* #### Veroboard / stripboard

As shown here, the intvlm8r is built onto a piece of Veroboard, aka stripboard.

<a href="https://www.jaycar.com.au/pc-boards-vero-type-strip-95mm-x-75mm/p/HP9540" target="_blank">Jaycar (AU)</a>

$AUD4.50

* #### Resistors

Resistors are used on the board for two purposes. They're either current-limiting the supply to the LEDs (the green one and the 2 optos) or providing pull-up or pull-down assistance to the IO pins. You should be able to find these just about anywhere: your Arduino/Pi supplier, local electronics hobby store, etc
* Green LED: 1 x 150R 1/4W
* Optos: 2 x 150R 1/4W
* Arduino pin A8: 1 x 4.7k 1/4W
* Arduino pin A2: 1 x 4.7k 1/4W

$AUD1


* #### Capacitor

I really love the DeadOn RTC, however SparkFun appear to have omitted the chip manufacturer's recommended power supply capacitor. I went with a 100pF ceramic.

<a href="https://au.element14.com/vishay/d101k20y5ph63l6r/ceramic-capacitor-100pf-100v-y5p/dp/1606155?st=100pf%20ceramic" target="_blank">Element 14</a>

$AUD0.30

* #### Miscellaneous

Header pins, jumpers, bolts, spacers, backmount, interconnecting wires.

$AUD10 (Approx)

### SUBTOTAL: $201.80

## Hardware - casing and mounts

* #### Pelican 1300 case

$95

* #### Camera Mount

(Manfrotto 357 Universal Quick Release Plate)	

$AUD85

* #### CCTV Camera Mount

$AUD15

* #### Ram Mounts

If your budget allows for it, check out some of the mounting options in the Ram Mounts range. Their <a href="https://www.rammount.com/search?query=c+size" target="_blank">"C Size" mounts</a> will take up to a 5kg (~10lb) load.




## SUBTOTAL: $195

# GRAND TOTAL: $AUD1081.80
# (Approx $USD 780)
