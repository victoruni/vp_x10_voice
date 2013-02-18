FILE(REMOVE_RECURSE
  "../src/vp_x10_voice/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_lisp"
  "../msg_gen/lisp/X10.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_X10.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
