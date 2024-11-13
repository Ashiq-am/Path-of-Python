def resizeGL(self, width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    aspect_ratio = width / height
    fov_degrees = 45.0
    near_clip = 0.1
    far_clip = 100.0

    # Calculate perspective projection matrix manually
    top = near_clip * math.tan(math.radians(fov_degrees / 2.0))
    bottom = -top
    left = bottom * aspect_ratio
    right = top * aspect_ratio

    glFrustum(left, right, bottom, top, near_clip, far_clip)
    glMatrixMode(GL_MODELVIEW)
