#project_utils.py

def plot_images(images, cls_true, cls_pred=None, smooth=True):
    import matplotlib.pyplot as plt_2
    import cv2
    assert len(images) == len(cls_true)

    # Create figure with sub-plots.
    fig, axes = plt_2.subplots(2, 2)
    
    # Adjust vertical spacing.
    if cls_pred is None:
        hspace = 0.3
    else:
        hspace = 0.6

    fig.subplots_adjust(hspace=hspace, wspace=0.3)

    # Interpolation type.
    if smooth:
        interpolation = 'spline16'
    else:
        interpolation = 'nearest'

    for i, ax in enumerate(axes.flat):
        # There may be less than 4 images, ensure it doesn't crash.
        if i < len(images):
            
            # Load image from file first
            img = cv2.imread(images[i])
            cv_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            # Plot image.
            ax.imshow(img, interpolation=interpolation)

            # Name of the true class.
            cls_true_name = cls_true[i]

            # Show true and predicted classes.
            if cls_pred is None:
                xlabel = "True: {0}".format(cls_true_name)
            else:
                # Name of the predicted class.
                cls_pred_name = class_names[cls_pred[i]]

                xlabel = "True: {0}\nPred: {1}".format(cls_true_name, cls_pred_name)

            # Show the classes as the label on the x-axis.
            ax.set_xlabel(xlabel)
        
        # Remove ticks from the plot.
        ax.set_xticks([])
        ax.set_yticks([])
    
    # Ensure the plot is shown correctly with multiple plots
    # in a single Notebook cell.
    plt_2.show()