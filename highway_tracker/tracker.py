import math

class EuclideanDistTracker:
    def __init__(self):
        self.center_points = {}
        self.id_count = 0
        
    def update(self, objects_rect):
        objects_bbs_ids = []
        for rect in objects_rect:
            x, y, w, h = rect #unpack data
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2
            # print(cx, cy)

   # print(cx, cy) jadikan komentar
            same_object_detected = False #a
            for id, pt in self.center_points.items():
               dist = math.hypot(cx - pt[0], cy - pt[1])
               if dist < 50:
                  self.center_points[id] = (cx, cy)
                  objects_bbs_ids.append([x, y, w, h, id])
                  same_object_detected = True
                  break

        return objects_bbs_ids #mengembalikan list objects_bbs_ids yang nanti akan disimpan dalam boxes_ids (di file main.py)

#   for id, pt in self.center_points.items():
#                  #prev code for 
#             # ADD CODE BELOW
#             if same_object_detected == False:
#                 self.center_points[self.id_count] = (cx, cy)
#                 objects_bbs_ids.append([x, y, w, h, self.id_count])
#                 self.id_count += 1 #id akan di increment untuk object id selanjutnya yang terdeteksi
# 		 print(self.center_points)
#          return objects_bbs_ids

# cv2.rectangle(roi, (x,y), (x+w, y+h), (0,255,0), 2)


