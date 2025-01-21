import seaborn as sns
def get_tips():
    tips = sns.load_dataset('tips')
    print(tips.head(3))
    return tips


if __name__ == '__main__':
    get_tips()