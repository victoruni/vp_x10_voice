; Auto-generated. Do not edit!


(cl:in-package vp_x10_voice-msg)


;//! \htmlinclude X10.msg.html

(cl:defclass <X10> (roslisp-msg-protocol:ros-message)
  ((command1
    :reader command1
    :initarg :command1
    :type cl:fixnum
    :initform 0)
   (command2
    :reader command2
    :initarg :command2
    :type cl:fixnum
    :initform 0)
   (repeatTime
    :reader repeatTime
    :initarg :repeatTime
    :type cl:fixnum
    :initform 0))
)

(cl:defclass X10 (<X10>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <X10>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'X10)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vp_x10_voice-msg:<X10> is deprecated: use vp_x10_voice-msg:X10 instead.")))

(cl:ensure-generic-function 'command1-val :lambda-list '(m))
(cl:defmethod command1-val ((m <X10>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vp_x10_voice-msg:command1-val is deprecated.  Use vp_x10_voice-msg:command1 instead.")
  (command1 m))

(cl:ensure-generic-function 'command2-val :lambda-list '(m))
(cl:defmethod command2-val ((m <X10>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vp_x10_voice-msg:command2-val is deprecated.  Use vp_x10_voice-msg:command2 instead.")
  (command2 m))

(cl:ensure-generic-function 'repeatTime-val :lambda-list '(m))
(cl:defmethod repeatTime-val ((m <X10>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vp_x10_voice-msg:repeatTime-val is deprecated.  Use vp_x10_voice-msg:repeatTime instead.")
  (repeatTime m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <X10>) ostream)
  "Serializes a message object of type '<X10>"
  (cl:let* ((signed (cl:slot-value msg 'command1)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'command2)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'repeatTime)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <X10>) istream)
  "Deserializes a message object of type '<X10>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'command1) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'command2) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'repeatTime) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<X10>)))
  "Returns string type for a message object of type '<X10>"
  "vp_x10_voice/X10")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'X10)))
  "Returns string type for a message object of type 'X10"
  "vp_x10_voice/X10")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<X10>)))
  "Returns md5sum for a message object of type '<X10>"
  "412ad5f78068f9ac88fb2866fbc7c142")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'X10)))
  "Returns md5sum for a message object of type 'X10"
  "412ad5f78068f9ac88fb2866fbc7c142")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<X10>)))
  "Returns full string definition for message of type '<X10>"
  (cl:format cl:nil "int16 command1~%int16 command2~%int16 repeatTime~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'X10)))
  "Returns full string definition for message of type 'X10"
  (cl:format cl:nil "int16 command1~%int16 command2~%int16 repeatTime~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <X10>))
  (cl:+ 0
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <X10>))
  "Converts a ROS message object to a list"
  (cl:list 'X10
    (cl:cons ':command1 (command1 msg))
    (cl:cons ':command2 (command2 msg))
    (cl:cons ':repeatTime (repeatTime msg))
))
