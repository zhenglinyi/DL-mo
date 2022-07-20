""" Example for MOGONET classification
"""
from train_test_zyh import train_test

if __name__ == "__main__":    
    data_folder = 'breast2'
    view_list = [1,2,3]
    num_epoch_pretrain = 500
    num_epoch = 2500
    lr_e_pretrain = 1e-3
    lr_e = 5e-4
    lr_c = 1e-3
    
    if data_folder == 'ROSMAP':
        num_class = 2
    if data_folder == 'BRCA':
        num_class = 5
    if data_folder == 'gbm'or data_folder =='breast2':
        num_class = 4
    if data_folder == '/home/zyh/MOGONET/LUAD2':
        num_class = 3
    if data_folder == '/home/zyh/MOGONET/sarcoma2':
        num_class = 6
    if data_folder == '/home/zyh/MOGONET/STAD2':
        num_class = 4
    train_test(data_folder, view_list, num_class,
               lr_e_pretrain, lr_e, lr_c, 
               num_epoch_pretrain, num_epoch)