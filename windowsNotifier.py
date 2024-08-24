'''
This is the official Windows client script for the simple-github-announcements project.

First priority is to make it work on Windows 10, and then Windows 11. 

Notes: Currently works with windows 10. Missing a tile

Seems that ToastGeneric requires path to app

'''

import winrt.windows.ui.notifications as notifications
import winrt.windows.data.xml.dom as dom

notificationManager = notifications.ToastNotificationManager;


template = notifications.ToastTemplateType.TOAST_IMAGE_AND_TEXT02;

xmlString = notifications.ToastNotificationManager.get_template_content(template)
print(xmlString.get_xml())

print()


# xmlString = "<toast><visual><binding template=\"ToastImageAndText02\"><image id=\"1\" src=\"file:///C:\\Users\\kgoel\\OneDrive - Synopsys, Inc\\Desktop\\myLearning\\simple-github-announcements-client\\grump.png\"/><text id=\"1\">This is some text</text><text id=\"2\">This is some longer text. I wish it was shorter. What if it were even shorter?</text></binding></visual></toast>"
xmlString = """
<toast><visual><binding template=\"ToastGeneric\"><image placement=\"appLogoOverride\" id=\"1\" hint-crop=\"circle\" src=\"file:///D:\\Code\\announcements\\simple-github-announcements-client\\grump.png\"/><text id=\"1\">This is some text</text><text id=\"2\">This is some longer text. I wish it was shorter. What if it were even shorter?</text></binding></visual><actions>
          <action content='See more details' arguments='action=viewDetails;contentId=351'/>
          <action content='Remind me later' arguments='action=remindLater;contentId=351'/>
      </actions></toast>
      """

# xmlString = """
# <toast>
#   <visual>
#     <binding template="ToastGeneric">
#     </binding>
#   </visual>
# </toast>
# """

# images = toastXml.getElementsByTagName("image");

# images = xmlString.get_elements_by_tag_name("image")

# print("Trying to print the value")

# print(images.item(0).attributes.get_named_item("src").inner_text)

# print("Now trying to assign the value")
# # print(images.item(0).get_xml())
# images.item(0).attributes.get_named_item("src").inner_text = "grumpy.png"

# print("Trying to print the value")

# print(images.item(0).attributes.get_named_item("src").inner_text)

# print("Problematic line succeeded")



# var textNodes = toastXml.getElementsByTagName("text");
# textNodes = xmlString.get_elements_by_tag_name("text")

# textNodes.item(0).inner_text = "Some text"

# print(xmlString.get_xml())



# for textNode in textNodes:

# textNodes.forEach(function (value, index) {
#     var textNumber = index + 1;
#     var text = "";
#     for (var j = 0; j < 10; j++) {
#         text += "Text input " + /*@static_cast(String)*/textNumber + " ";
#     }
#     value.appendChild(toastXml.createTextNode(text));
# });


# // Create a toast notification from the XML, then create a ToastNotifier object
# // to send the toast.


xmlDoc = dom.XmlDocument()

xmlDoc.load_xml(xmlString)

print(xmlDoc.get_xml())

toast = notifications.ToastNotification(xmlDoc);

notificationManager.create_toast_notifier(r"C:\Python312\python.exe").show(toast);
# notificationManager.create_toast_notifier("Notifire").show(toast);


# # Create the toast notification
# toast_notification = notifications.ToastNotification(xml_document)

# # Get the toast notification manager
# toast_notification_manager = notifications.ToastNotificationManager.create_toast_notifier(r"D:\Code\Android\FTB_V28.9_Portable\Fire Toolbox V28.9\Fire Toolbox.exe")

# # Show the notification
# toast_notification_manager.show(toast_notification)

# print("Notification sent!")
