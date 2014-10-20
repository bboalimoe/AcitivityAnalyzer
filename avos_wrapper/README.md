

#avos

====

Another Python wrapper for avoscloud.com



### Develop

python setup.py develop


### Quick start

	# Inherit from AVObject
	from avos.avos import AVObject

	# Child class name is your AVOS class name
	class TestClass(AVObject):
    	def __init__(self):
        	super(TestClass, self).__init__()

	# Set your app_id and app_key
    TestClass.app_settings = [app_id, app_key]


    # Create object
    new_ob = {}
    res = TestClass.save(new_ob)
    if 'createdAt' in json.loads(res.content):
        print 'Succeeded!'

    # Query
    TestClass.get(where={...},limit=N, ... )


    # Patch

    TestClass.patch(patch_ob_list)
    TestClass.save_all(ob_list)
    TestClass.update_all(ob_list)
    TestClass.remove_all(ob_list)


    # ... ...




### pre-beta




