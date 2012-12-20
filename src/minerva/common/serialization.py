import messages_pb2 as messages

class Serialization(object):
    
    @staticmethod
    def create_location(lat, lon):
        location = messages.Location()
        location.longitude = lon
        location.latitude = lat
        return location
    
    @staticmethod        
    def serialize_sendquery(user_id, query, page=1, lat=0.0, lon=0.0):
        send_query = messages.SendQuery()
        send_query.user_id = user_id
        send_query.query = query
        send_query.page = page
        send_query.location.CopyFrom(Serialization.create_location(lat, lon))
        return send_query.SerializeToString()
    
    @staticmethod
    def deserialize_sendquery(serialized):
        send_query = messages.SendQuery()
        send_query.ParseFromString(serialized) 
        return send_query
    
    @staticmethod        
    def serialize_sendqueryresponse(results):
        send_query_response = messages.SendQueryResponse()
        for result in results:
            query_result = send_query_response.query_result.add()
            query_result.title = result[0]
            query_result.url = result[1]
        return send_query_response.SerializeToString()
    
    @staticmethod
    def deserialize_sendqueryresponse(serialized):
        send_query_response = messages.SendQueryResponse()
        send_query_response.ParseFromString(serialized) 
        return send_query_response
    
    @staticmethod
    def create_user(age, department, degree, degree_year):
        user = messages.User()
        user.age = age
        user.department = department
        user.degree = degree
        user.degree_year = degree_year
        return user
        
    @staticmethod
    def create_networkdetails(bandwidth, ip='0.0.0.0'):
        network_details = messages.NetworkDetails()
        network_details.ip = ip
        network_details.bandwidth = bandwidth
        return network_details
        
    @staticmethod
    def create_mobiledevice(brand, model, audio_support, video_support, os, os_version):
        mobile_device = messages.MobileDevice()
        mobile_device.brand = brand
        mobile_device.model = model
        mobile_device.audio_support = audio_support
        mobile_device.video_support = video_support
        mobile_device.mobile_os.CopyFrom(Serialization.create_mobileos(os, os_version))
        return mobile_device
        
    @staticmethod
    def create_mobileos(os, os_version):
        mobile_os = messages.MobileOS()
        mobile_os.os = os
        mobile_os.os_version = os_version
        return mobile_os
    
    @staticmethod
    def create_rsakey(public_key_mod, public_key_exp):
        rsakey = messages.RSAKey()
        rsakey.mod = public_key_mod
        rsakey.exp = public_key_exp
        return rsakey

    @staticmethod        
    def serialize_registeruser(username, user, mobile_device, network_details, 
                               public_key_mod, public_key_exp, symmetric_key):
        register_user = messages.RegisterUser()
        register_user.username = username
        register_user.user.CopyFrom(user)
        register_user.mobile_device.CopyFrom(mobile_device)
        register_user.network_details.CopyFrom(network_details)
        register_user.public_key.CopyFrom(Serialization.create_rsakey(public_key_mod,
                                                                      public_key_exp))
        register_user.symmetric_key = symmetric_key
        return register_user.SerializeToString()
    
    @staticmethod
    def deserialize_registeruser(serialized):
        register_user = messages.RegisterUser()
        register_user.ParseFromString(serialized) 
        return register_user
    
    @staticmethod        
    def serialize_registeruserresponse(user_id):
        register_userresponse = messages.RegisterUserResponse()
        register_userresponse.user_id = user_id
        return register_userresponse.SerializeToString()
    
    @staticmethod
    def deserialize_registeruserresponse(serialized):
        register_userresponse = messages.RegisterUserResponse()
        register_userresponse.ParseFromString(serialized) 
        return register_userresponse
    
    @staticmethod        
    def serialize_getpublickey(username):
        getpublickey = messages.GetPublicKey()
        getpublickey.username = username
        return getpublickey.SerializeToString()
    
    @staticmethod
    def deserialize_getpublickey(serialized):
        getpublickey = messages.GetPublicKey()
        getpublickey.ParseFromString(serialized) 
        return getpublickey
    
    @staticmethod        
    def serialize_getpublickeyresponse(public_key):
        getpublickeyresponse = messages.GetPublicKeyResponse()
        getpublickeyresponse.public_key.CopyFrom(Serialization.create_rsakey(str(public_key.n), 
                                                                             str(public_key.e)))
        return getpublickeyresponse.SerializeToString()
    
    @staticmethod
    def deserialize_getpublickeyresponse(serialized):
        getpublickeyresponse = messages.GetPublicKeyResponse()
        getpublickeyresponse.ParseFromString(serialized) 
        return getpublickeyresponse
    