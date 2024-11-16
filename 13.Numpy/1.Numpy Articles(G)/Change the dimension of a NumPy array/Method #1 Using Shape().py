# importing numpy
import numpy as np


def main():
    # initialising array
    print('Initialised array')
    gfg = np.array([1, 2, 3, 4])
    print(gfg)

    # checking current shape
    print('current shape of the array')
    print(gfg.shape)

    # modifying array according to new dimensions
    print('changing shape to 2,3')
    gfg.shape = (2, 2)
    print(gfg)


if __name__ == "__main__":
    main()
