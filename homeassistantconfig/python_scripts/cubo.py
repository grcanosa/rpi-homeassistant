def get_info_from_full_string(full):
  info = {}
  spli = full.split(";")
  action=spli[0].split("=")[1]
  args=spli[1].split(",")
  for a in args:
    s = a.strip().split("=")
    info[s[0]]= s[1]
  info["action"]=action
  return info 

#logger.info("CUBO")

full = data.get("full")
info = get_info_from_full_string(full)

#logger.info(state)
#logger.info(info)
service_data = {}
LUZ="light.0x680ae2fffeb15341_light"
service_data["entity_id"]=LUZ
light_state = hass.states.get(LUZ).as_dict()
#logger.info(light_state.as_dict())
brillo = light_state["attributes"]["brightness"]
if info["action"] == "flip90":
  hass.services.call("light","toggle",service_data,False)
elif "rotate" in info["action"]:
  angle_per = abs(float(info["angle"])) / 180
  sign = 1 if info["action"] == "rotate_right" else -1
  add_brillo = sign * angle_per * 255
  new_brillo = brillo + add_brillo
  service_data["brightness"] = new_brillo
  logger.info("old_brillo"+str(brillo)+" add brillo"+str(add_brillo)+" New brillo is "+str(new_brillo))
  hass.services.call("light","turn_on",service_data,False)
elif info["action"] == "flip180":  
  logger.info("Change color, TBD")

