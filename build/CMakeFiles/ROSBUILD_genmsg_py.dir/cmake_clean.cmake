FILE(REMOVE_RECURSE
  "../src/vp_x10_voice/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/vp_x10_voice/msg/__init__.py"
  "../src/vp_x10_voice/msg/_X10.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
