
(cl:in-package :asdf)

(defsystem "vp_x10_voice-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "X10" :depends-on ("_package_X10"))
    (:file "_package_X10" :depends-on ("_package"))
  ))