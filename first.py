import cv2
import numpy as np

# 1. 去掉了“软件”两个字，回到你真实的路径
img_path = 'D:/vision01/images/photo.jpeg'

# 魔法读取（你已经验证过没问题了）
img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_COLOR)

if img is None:
    print("读取失败：路径对了，但图片格式可能损坏")
else:
    print("图片尺寸: ", img.shape)

    # 显示图片
    cv2.imshow("test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 2. 保存路径也去掉“软件”
    out_path = 'D:/vision01/out/result.jpg'
    cv2.imencode('.jpg', img)[1].tofile(out_path)
    print("已保存到: ", out_path)