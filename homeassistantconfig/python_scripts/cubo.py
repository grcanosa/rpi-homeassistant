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

logger.info("CUBO")

full = data.get("full")
info = get_info_from_full_string(full)

#logger.info(state)
logger.info(info)
service_data = {}
service_data["entity_id"]="light.0x680ae2fffeb15341_light"
if info["action"] == "flip90":
  hass.services.call("light","toggle",service_data,False)