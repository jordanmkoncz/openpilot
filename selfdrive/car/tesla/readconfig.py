import ConfigParser

default_config_file_path = '/data/bb_openpilot.cfg'

class ConfigFile(object):
  config_file_r = 'r'
  config_file_w = 'wb'

  ### Do NOT modify here, modify in /data/bb_openpilot.cfg and reboot
  def read(self, into, config_path):
      configr = ConfigParser.ConfigParser()
      file_changed = False

      try:
        configr.read(config_path)
        fd = open(config_path, "r")
        self.current_file_contents = fd.read()
        fd.close()
      except:
        self.current_file_contents = ""
        print("no config file, creating with defaults...")

      main_section = 'OP_CONFIG'
      config = ConfigParser.RawConfigParser(allow_no_value=True)
      config.add_section(main_section)

      #force_pedal_over_cc -> forcePedalOverCC
      into.forcePedalOverCC, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'force_pedal_over_cc', type = bool,
        default_value = False,
        comment = 'Forces the use of Tesla Pedal over ACC completely disabling the Tesla CC'
      )
      file_changed |= didUpdate
      
      #enable_hso -> enableHSO
      into.enableHSO, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'enable_hso', type = bool,
        default_value = True,
        comment = 'Enables Human Steering Override (HSO) feature which allows you to take control of the steering wheel and correct the course of the car without disengaging OpenPilot lane keep assis (LKS, lateral control)'
      )
      file_changed |= didUpdate

      #enable_das_emulation -> enableDasEmulation
      into.enableALCA, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'enable_alca', type = bool,
        default_value = True,
        comment = 'Enables the Adaptive Lane Change Assist (ALCA) feature which will automatically change lanes when driving above 18 MPH (29 km/h) by just pushing 1/2 way on your turn signal stalk; turn signal will remain on for the duration of lane change'
      )
      file_changed |= didUpdate

      #enable_das_emulation -> enableDasEmulation
      into.enableDasEmulation, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'enable_das_emulation', type = bool,
        default_value = False,
        comment = 'The secret sauce of IC/CID integration; this feature makes the Panda generate all the CAN messages needed for IC/CID integration that mimiinto the AP interface'
      )
      file_changed |= didUpdate

      #enable_radar_emulation -> enableRadarEmulation
      into.enableRadarEmulation, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'enable_radar_emulation', type = bool,
        default_value = False,
        comment = 'The secret sauce to make the Tesla Radar work; this feature make the Panda generate all the CAN messages needed by the Tesla Bosch Radar to operate'
      )
      file_changed |= didUpdate

      #enable_roll_angle_correction -> enableRollAngleCorrection
      into.enableSpeedVariableDesAngle, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'enable_speed_variable_angle', type = bool,
        default_value = True,
        comment = ''
      )
      file_changed |= didUpdate

      #enable_roll_angle_correction -> enableRollAngleCorrection
      into.enableRollAngleCorrection, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'enable_roll_angle_correction', type = bool,
        default_value = False,
        comment = ''
      )
      file_changed |= didUpdate

      #enable_feed_forward_angle_correction -> enableFeedForwardAngleCorrection
      into.enableFeedForwardAngleCorrection, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'enable_feed_forward_angle_correction', type = bool,
        default_value = True,
        comment = ''
      )
      file_changed |= didUpdate

      #enable_driver_monitor -> enableDriverMonitor
      into.enableDriverMonitor, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'enable_driver_monitor', type = bool,
        default_value = True,
        comment = 'When turned off, the OpenPilot is tricked into thinking you have the hands on the sterring wheel all the time'
      )
      file_changed |= didUpdate

      #enable_show_car -> enableShowCar
      into.enableShowCar, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'enable_show_car', type = bool,
        default_value = True,
        comment = 'Shows a Tesla car in the limitted UI mode instead of the triangle that identifies the lead car; this is only used if you do not have IC/CID integration'
      )
      file_changed |= didUpdate

      #enable_show_logo -> enableShowLogo
      into.enableShowLogo, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'enable_show_logo', type = bool,
        default_value = True,
        comment = 'Shows a Tesla red logo on the EON screen when OP is not enabled'
      )
      file_changed |= didUpdate

      #has_noctua_fan -> hasNoctuaFan
      into.hasNoctuaFan, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'has_noctua_fan', type = bool,
        default_value = False,
        comment = 'Enables control of Noctua fan (at higher RPMS) when you have a Noctua fan installed'
      )
      file_changed |= didUpdate

      #limit_battery_minmax -> limitBatteryMinMax
      into.limitBatteryMinMax, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'limit_battery_minmax', type = bool,
        default_value = True,
        comment = 'Enables battery charging limits; the battery will start charging when battery percentage is below limit_battery_min and will stop charging when battery percentage is above limit_battery_max'
      )
      file_changed |= didUpdate

      #limit_battery_min -> limitBattery_Min
      into.limitBattery_Min, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'limit_battery_min', type = int,
        default_value = 60,
        comment = 'See limit_battery_minmax'
      )
      file_changed |= didUpdate

      #limitBattery_Max -> limitBattery_Max
      into.limitBattery_Max, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'limit_battery_max', type = int,
        default_value = 80,
        comment = 'See limit_battery_minmax'
      )
      file_changed |= didUpdate

      #block_upload_while_tethering -> blockUploadWhileTethering
      into.blockUploadWhileTethering, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'block_upload_while_tethering', type = bool,
        default_value = False,
        comment = 'This setting will block uploading OP videos to Comma when you are tethering through the phone. You should set the tether_ip to the first 3 values that your phone provides as IP when you tether. This is phone/carrier specific. For example iPhone give addresses like 172.20.10.x so you would enter 172.20.10.'
      )
      file_changed |= didUpdate

      #tether_ip -> tetherIP
      into.tetherIP, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'tether_ip', type = str,
        default_value = "127.0.0.",
        comment = 'See block_upload_while_tethering'
      )
      file_changed |= didUpdate

      #use_tesla_gps -> useTeslaGPS
      into.useTeslaGPS, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'use_tesla_gps', type = bool,
        default_value = False,
        comment = 'This setting makes OP to use Tesla GPS data instead of the GPS that comes with the gray panda; both GPS systems use Ublox and both are very close in accuracy; this also allows one to use a White Panda and still have map integration'
      )
      file_changed |= didUpdate

      #use_tesla_map_data -> useTeslaMapData
      into.useTeslaMapData, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'use_tesla_map_data', type = bool,
        default_value = False,
        comment = 'This setting (which requires root) allows OP to use Tesla navigation map data (under development)'
      )
      file_changed |= didUpdate

      #use_analog_when_no_eon -> useAnalogWhenNoEon
      into.hasTeslaIcIntegration, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'has_tesla_ic_integration', type = bool,
        default_value = False,
        comment = 'This setting (in conjunction with enable_radar_emulation) help create the IC integration'
      )
      file_changed |= didUpdate

      #use_analog_when_no_eon -> useAnalogWhenNoEon
      into.useAnalogWhenNoEon, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'use_analog_when_no_eon', type = bool,
        default_value = False,
        comment = 'Not used at the moment; should be False'
      )
      file_changed |= didUpdate
      
      #use_tesla_radar -> useTeslaRadar
      into.useTeslaRadar, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'use_tesla_radar', type = bool,
        default_value = False,
        comment = 'Set this setting to True if you have a Tesla Bosch Radar installed (works in conjunction with enable_radar_emulation)'
      )
      file_changed |= didUpdate

      #use_without_harness = useWithoutHarness
      into.useWithoutHarness, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'use_without_harness', type = bool,
        default_value = False,
        comment = 'Not used at the moment; should be False'
      )
      file_changed |= didUpdate

      #radar_vin -> into.radarVIN
      default_radar_vin = '"                 "'
      into.radarVIN, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'radar_vin', type = str,
        default_value = default_radar_vin,
        comment = 'If you used an aftermarket Tesla Bosch Radar that already has a coded VIN, you will have to enter that VIN value here'
      )
      file_changed |= didUpdate
      if into.radarVIN == '':
        into.radarVIN = default_radar_vin
        file_changed = True

      #enable_ldw = enableLdw
      into.enableLdw, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'enable_ldw', type = bool,
        default_value = True,
        comment = 'Enable the Lane Departure Warning (LDW) feature; this feature warns the driver is the car gets too close to one of the lines when driving above 45 MPH (72 km/h) without touching the steering wheel and when the turn signal is off'
      )
      file_changed |= didUpdate

      #radar_offset -> radarOffset
      into.radarOffset, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'radar_offset', type = float,
        default_value = 0,
        comment = 'If your Tesla Bosch Radar is not centered on the car, this value will allow to enter a correction offset'
      )
      file_changed |= didUpdate

      #radar_epas_type -> radarEpasType
      into.radarEpasType, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'radar_epas_type', type = int,
        default_value = 0,
        comment = 'Depending on the source of your Tesla Bosch Radar (older or newer Model S or Model X), this setting has to match what the radar was programmed to recognize as EPAS; values are between 0 and 4; finding the right one is trial and error'
      )
      file_changed |= didUpdate

      #radar_position -> radarPosition
      into.radarPosition, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'radar_position', type = int,
        default_value = 0,
        comment = 'Depending on the source of your Tesla Bosch Radar (older or newer Model S or Model X), this setting has to match what the radar was programmed to have a position (Model S, Model S facelift, Model X); values are between 0 and 3; finding the right one is trial and error'
      )
      file_changed |= didUpdate

      #do_auto_update -> doAutoUpdate
      into.doAutoUpdate, didUpdate = self.read_config_entry(
        config, configr, section = main_section,
        entry = 'do_auto_update', type = bool,
        default_value = True,
        comment = 'Set this setting to False if you do not want OP to autoupdate every time you reboot and there is a change on the repo'
      )
      file_changed |= didUpdate

      if file_changed:
        did_write = True
        with open(config_path, self.config_file_w) as configfile:
          config.write(configfile)
      else:
        did_write = False

      # Remove double quotes from VIN (they are required for empty case)
      into.radarVIN = into.radarVIN.replace('"', '')
      return did_write

  def read_config_entry(self, config, configr, section, entry, type, default_value, comment):
      updated = self.update_comment(config, section, entry, default_value, comment)
      result = None
      try:
        if type == bool:
          result = configr.getboolean(section, entry)
        elif type == int:
          result = configr.getint(section, entry)
        elif type == float:
          result = configr.getfloat(section, entry)
        else:
          result = configr.get(section, entry)
      except:
        result = default_value
        updated = True
      config.set(section, entry, result)
      return result, updated

  def update_comment(self, config, section, entry, default_value, comment):
      new_comment = ("# " + entry + ": " + comment + " (Default: " + str(default_value) + ")").lower()
      if self.current_file_contents.find(new_comment) == -1:
        config.set(section, new_comment)
        updated = True
      else:
        updated = False
      return updated

class CarSettings(object):
  def __init__(self, optional_config_file_path = default_config_file_path):
    config_file = ConfigFile()
    self.did_write_file = config_file.read(self, config_path = optional_config_file_path)

  def get_value(self, name_of_variable):
    return_val = None
    exec("%s = self.%s" % ('return_val', name_of_variable))
    return return_val

# Legacy support
def read_config_file(into, config_path = default_config_file_path):
  config_file = ConfigFile()
  config_file.read(into, config_path)