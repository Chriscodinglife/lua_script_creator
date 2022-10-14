-- MBP, Chris O

-- VARIABLES
local logo="<logo_image>"

local product="<product_image>"

local description = [[
<hr/>
<center><h2><package_name></h2></center>
<p>
<center><img  width=192 height=108 src=']] .. product .. [['/></center>
<hr/>
<p>
<center><img width=60 height=60 src=']] .. logo .. [['/></center>
<p>
<center>For Customer Support contact us here: <a hrep="<support_link>"><store_name></a></center>
<p>Thank you for purchasing our Stream Package!
<p>Use this menu to quickly set your stream up
<hr/>
<p>
<p>Use this manual to help you in getting setup:
<p><manual>
<p>
<hr/>
<p>
</p>]]

-- IMPORT
obs = obslua


--FUNCTIONS 
function script_description()
    
    return description

end

function scene_exists(scene_name)

	local scene_names = obs.obs_frontend_get_scene_names()
	local value = 0

	for i, name in ipairs(scene_names) do
		if string.find(scene_names[i], scene_name) then
			value = value + 1
		end
	end

	return value
	
end

function create_scene(scene_name)

	if scene_exists(scene_name) >= 1 then
		scene_name = scene_name .. " " .. scene_exists(scene_name)
	end

	local new_scene = obs.obs_scene_create(scene_name)

	obs.obs_frontend_set_current_scene(obs.obs_scene_get_source(new_scene))
	local current_scene = obs.obs_frontend_get_current_scene()
	local scene = obs.obs_scene_from_source(current_scene)

	obs.obs_scene_release(new_scene)
	obs.obs_scene_release(scene)

	return new_scene, scene

end

function create_loop_overlay(file_location, name, new_scene, scene, xpos, ypos, xscale, yscale)

	local pos = obs.vec2()
	local scale = obs.vec2()

	local overlay_settings = obs.obs_data_create()
	obs.obs_data_set_string(overlay_settings, "local_file", script_path() .. file_location)
	obs.obs_data_set_bool(overlay_settings, "looping", true)
	local overlay_source = obs.obs_source_create("ffmpeg_source", name, overlay_settings, nil)
	obs.obs_scene_add(new_scene, overlay_source)

	local overlay_sceneitem = obs.obs_scene_find_source(scene, name)
	local overlay_location = pos
	local overlay_scale = scale
	if overlay_sceneitem then
		overlay_location.x = xpos
		overlay_location.y = ypos
		overlay_scale.x = xscale
		overlay_scale.y = yscale
		obs.obs_sceneitem_set_pos(overlay_sceneitem, overlay_location)
		obs.obs_sceneitem_set_scale(overlay_sceneitem, overlay_scale)
	end

	obs.obs_source_update(overlay_source, overlay_settings)
	obs.obs_data_release(overlay_settings)
	obs.obs_source_release(overlay_source)

end

function create_image(file_location, name, new_scene, scene, xpos, ypos, xscale, yscale)

	local pos = obs.vec2()
	local scale = obs.vec2()

	local image_settings = obs.obs_data_create()
	obs.obs_data_set_string(image_settings, "file", script_path() .. file_location)
	local image_source = obs.obs_source_create("image_source", name, image_settings, nil)
	obs.obs_scene_add(new_scene, image_source)

	local image_sceneitem = obs.obs_scene_find_source(scene, name)
	local image_location = pos
	local image_scale = scale
	if image_sceneitem then
		image_location.x = xpos
		image_location.y = ypos
		image_scale.x = xscale
		image_scale.y = yscale
		obs.obs_sceneitem_set_pos(image_sceneitem, image_location)
		obs.obs_sceneitem_set_scale(image_sceneitem, image_scale)
	end

	obs.obs_source_update(image_source, image_settings)
	obs.obs_data_release(image_settings)
	obs.obs_source_release(image_source)

end

local black_color = 4278190080
function create_text(face, size, style, text, align, color, outline, outline_color, outline_size, name, new_scene, scene, x, y)

	local pos = obs.vec2()
	local scale = obs.vec2()

	local text_settings = obs.obs_data_create()
	local text_font_object = obs.obs_data_create_from_json('{}')
	obs.obs_data_set_string(text_font_object, "face", face)
	obs.obs_data_set_int(text_font_object, "flags", 0)
	obs.obs_data_set_int(text_font_object, "size", size)
	obs.obs_data_set_string(text_font_object, "style", style)
	obs.obs_data_set_obj(text_settings, "font", text_font_object)
	obs.obs_data_set_string(text_settings, "text", text)
	obs.obs_data_set_string(text_settings, "align", align)

	if color then
		obs.obs_data_set_int(text_settings, "color", color)
	end
	if outline then
		obs.obs_data_set_bool(text_settings, "outline", outline)
		obs.obs_data_set_int(text_settings, "outline_color", outline_color)
		obs.obs_data_set_int(text_settings, "outline_size", outline_size)
	end

	local text_source = obs.obs_source_create("text_gdiplus", name, text_settings, nil)
	obs.obs_scene_add(new_scene, text_source)
	
	local text_sceneitem = obs.obs_scene_find_source(scene, name)
	local text_location = pos
	if text_sceneitem then
		text_location.x = x
		text_location.y = y
		obs.obs_sceneitem_set_pos(text_sceneitem, text_location)
	end

	obs.obs_source_update(text_source, text_settings)
	obs.obs_data_release(text_settings)
	obs.obs_data_release(text_font_object)
	obs.obs_source_release(text_source)

end

function create_welcome_scene()

	scene_name = "Welcome"
	new_scene, scene = create_scene(scene_name)

	create_loop_overlay("Main_Design_Title/Main_Design_Title_1920_1080.webm",  scene_name .. " BG", new_scene, scene, 0, 0, 1, 1)

	create_text("<welcome_text_font>", 000, "<welcome_text_style>", "<welcome_text>", "center", _, true, black_color, 9, scene_name .. " Text", new_scene, scene, 360, 960)

end

function create_starting_soon_scene()

	scene_name = "Starting Soon"
	new_scene, scene = create_scene(scene_name)

	create_loop_overlay("Screen/Blank_Screen_1920_1080.webm",  scene_name .. " BG", new_scene, scene, 0, 0, 1, 1)

	create_loop_overlay("Screen/Starting_Soon_Screen_1920_1080.webm",  scene_name .. " Overlay", new_scene, scene, 0, 0, 1, 1)

end

function create_be_right_back_scene()

	scene_name = "Be Right Back"
	new_scene, scene = create_scene(scene_name)

	create_loop_overlay("Screen/Blank_Screen_1920_1080.webm",  scene_name .. " BG", new_scene, scene, 0, 0, 1, 1)

	create_loop_overlay("Screen/Be_Right_Back_Screen_1920_1080.webm",  scene_name .. " Overlay", new_scene, scene, 0, 0, 1, 1)

end

function create_thanks_for_watching_scene()

	scene_name = "Thanks For Watching"
	new_scene, scene = create_scene(scene_name)

	create_loop_overlay("Screen/Blank_Screen_1920_1080.webm",  scene_name .. " BG", new_scene, scene, 0, 0, 1, 1)

	create_loop_overlay("Screen/Thanks_For_Watching_Screen_1920_1080.webm",  scene_name .. " Overlay", new_scene, scene, 0, 0, 1, 1)

end

function import_all_scenes()

	create_welcome_scene()
	create_starting_soon_scene()
	create_be_right_back_scene()
	create_thanks_for_watching_scene()

	local scene_names = obs.obs_frontend_get_scene_names()
	local scene_list = obs.obs_frontend_get_scenes()
	
	for i, name in ipairs(scene_names) do
		if scene_names[i] == "Welcome" then
			scene = scene_list[i]
			obs.obs_frontend_set_current_scene(scene)
			break
		end
	end
	
	for i, scene in ipairs(scene_list) do
        obs.obs_source_release(scene)
    end

end


function script_properties()
	local properties = obs.obs_properties_create()
	
	--buttons
	local create_all_scenes_btn = obs.obs_properties_add_button(properties, "create_all_scenes", "Quick Setup", import_all_scenes)
	obs.obs_property_set_long_description(create_all_scenes_btn, "Insert all available scenes from this kit to your current OBS Session.")

	local create_welcome_scene_btn = obs.obs_properties_add_button(properties, "create_welcome_scene", "Import Welcome Scene", create_welcome_scene)
	obs.obs_property_set_long_description(create_welcome_scene_btn, "Insert the Welcome scene to your OBS Session.")

	local create_starting_soon_scene_btn = obs.obs_properties_add_button(properties, "create_starting_soon_scene", "Import Starting Soon Scene", create_starting_soon_scene)
	obs.obs_property_set_long_description(create_starting_soon_scene_btn, "Insert the Starting Soon scene to your OBS Session.")

	local create_be_back_scene_btn = obs.obs_properties_add_button(properties, "create_be_back_scene", "Import Be Right Back Scene", create_be_right_back_scene)
	obs.obs_property_set_long_description(create_be_back_scene_btn, "Insert the Be Right Back scene to your OBS Session.")

	local create_thanks_scene_btn = obs.obs_properties_add_button(properties, "create_later_scene", "Import Thanks For Watching Scene", create_thanks_for_watching_scene)
	obs.obs_property_set_long_description(create_thanks_scene_btn, "Insert the Thanks For Watching scene to your OBS Session.")

	return properties

end