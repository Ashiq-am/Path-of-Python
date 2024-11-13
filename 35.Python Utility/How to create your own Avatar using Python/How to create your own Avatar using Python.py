# Python program to create custom avatars

# importing the require package
import py_avataaars as pa

# assigning various parameters to our avatar
avatar = pa.PyAvataaar(style=pa.AvatarStyle.CIRCLE,
					skin_color=pa.SkinColor.LIGHT,
					hair_color=pa.HairColor.AUBURN,
					facial_hair_type=pa.FacialHairType.MOUSTACHE_MAGNUM,
					top_type=pa.TopType.SHORT_HAIR_SHAGGY_MULLET,
					mouth_type=pa.MouthType.SCREAM_OPEN,
					eye_type=pa.EyesType.SQUINT,
					eyebrow_type=pa.EyebrowType.RAISED_EXCITED_NATURAL,
					nose_type=pa.NoseType.DEFAULT,
					accessories_type=pa.AccessoriesType.PRESCRIPTION_02,
					clothe_type=pa.ClotheType.HOODIE,
					clothe_graphic_type=pa.ClotheGraphicType.BAT,)

# rendering the avatar in png format
avatar.render_png_file("AVATAR_2.png")
