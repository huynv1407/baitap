import cv2
path = 'out.jpg'
image = cv2.imread(path)
window_name = 'Image'
# start_point = (int(38.224264000000005 * 2.7781512605042016 ), int(2339 - (807.164248 * 2.7779097387173395)))
# end_point = (int(42.645576000000005 * 2.7781512605042016 ), int(2339 - (815.102248 * 2.7779097387173395)))

start_point = (int(38.224264000000005 ), int(2339 - (807.164248 * 2.7779097387173395)))
end_point = (int(42.645576000000005 * 2.7781512605042016 ), int(2339 - (815.102248 * 2.7779097387173395)))


# start_point = (10, 10)
# end_point = (20, 20)
color = (225, 0, 0)
thinkness = 2
image = cv2.rectangle(image, start_point, end_point, color, thinkness)
cv2.imshow(window_name, image)
cv2.waitKey(0)



# 38.224264000000005, 807.164248, 42.645576000000005, 815.102248
# height: 842, width: 595 ---PDF
# height:  2339 , width:  1653 ---Image
# height 0.3599828986746473 width 0.3599516031457955