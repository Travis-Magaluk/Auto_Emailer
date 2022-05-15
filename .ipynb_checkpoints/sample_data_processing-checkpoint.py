{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "430f17d5",
   "metadata": {},
   "source": [
    "# Sample Email Creation\n",
    "\n",
    "\n",
    "## Exploring email based on spreadsheet values. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3972e277",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "57287e9d",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>First Name</th>\n",
       "      <th>Last Name</th>\n",
       "      <th>Email</th>\n",
       "      <th>Health Screening</th>\n",
       "      <th>Health Assessment</th>\n",
       "      <th>Digital Coaching Program</th>\n",
       "      <th>First Activity Campaign</th>\n",
       "      <th>Second Activity Campaign</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Travis</td>\n",
       "      <td>Magaluk</td>\n",
       "      <td>travis.magaluk@wasatchacademy.org</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>T$</td>\n",
       "      <td>M$</td>\n",
       "      <td>twmagalu@gmail.com</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  First Name Last Name                              Email Health Screening  \\\n",
       "0     Travis   Magaluk  travis.magaluk@wasatchacademy.org              Yes   \n",
       "1         T$        M$                 twmagalu@gmail.com              Yes   \n",
       "\n",
       "  Health Assessment Digital Coaching Program First Activity Campaign  \\\n",
       "0               Yes                      Yes                     Yes   \n",
       "1               Yes                       No                      No   \n",
       "\n",
       "  Second Activity Campaign  \n",
       "0                      Yes  \n",
       "1                       No  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "email_list = pd.read_csv(\"Sample Data.csv\")\n",
    "display(email_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "1a3544e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def completed_check(item_list, i, output):\n",
    "    if item_list[i]=='Yes':\n",
    "        completed.append(output)\n",
    "    else:\n",
    "        un_completed.append(output)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "d062a8be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0    Yes\n",
      "1    Yes\n",
      "Name: Health Screening, dtype: object, 0    Yes\n",
      "1    Yes\n",
      "Name: Health Assessment, dtype: object, 0    Yes\n",
      "1     No\n",
      "Name: Digital Coaching Program, dtype: object, 0    Yes\n",
      "1     No\n",
      "Name: First Activity Campaign, dtype: object, 0    Yes\n",
      "1     No\n",
      "Name: Second Activity Campaign, dtype: object]\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/rg/3mv_js5n6lq2h93ynk_9vz_m0000gp/T/ipykernel_13246/632787318.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     29\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     30\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrequirements\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 31\u001b[0;31m         \u001b[0mcompleted_check\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrequirement_lists\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mi\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrequirements\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     32\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     33\u001b[0m \u001b[0;31m#     if all_health_screen[idx]=='Yes':\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/var/folders/rg/3mv_js5n6lq2h93ynk_9vz_m0000gp/T/ipykernel_13246/2336270366.py\u001b[0m in \u001b[0;36mcompleted_check\u001b[0;34m(item_list, i, output)\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mcompleted_check\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mitem_list\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mi\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moutput\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m     \u001b[0;32mif\u001b[0m \u001b[0mitem_list\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m==\u001b[0m\u001b[0;34m'Yes'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m         \u001b[0mcompleted\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0moutput\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m     \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m         \u001b[0mun_completed\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0moutput\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/miniconda3/lib/python3.9/site-packages/pandas/core/generic.py\u001b[0m in \u001b[0;36m__nonzero__\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m   1535\u001b[0m     \u001b[0;34m@\u001b[0m\u001b[0mfinal\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1536\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__nonzero__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1537\u001b[0;31m         raise ValueError(\n\u001b[0m\u001b[1;32m   1538\u001b[0m             \u001b[0;34mf\"The truth value of a {type(self).__name__} is ambiguous. \"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1539\u001b[0m             \u001b[0;34m\"Use a.empty, a.bool(), a.item(), a.any() or a.all().\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all()."
     ]
    }
   ],
   "source": [
    "# Get all the Names, Email Addreses, Status on Screening\n",
    "\n",
    "all_names = email_list['First Name'] + \" \" + email_list['Last Name']\n",
    "all_emails = email_list['Email']\n",
    "all_health_screen = email_list['Health Screening']\n",
    "all_health_assessment = email_list['Health Assessment']\n",
    "all_digital_coaching = email_list['Digital Coaching Program']\n",
    "all_first_activity = email_list['First Activity Campaign']\n",
    "all_second_activity = email_list['Second Activity Campaign']\n",
    "\n",
    "requirement_lists = [all_health_screen, all_health_assessment, all_digital_coaching, all_first_activity, all_second_activity]\n",
    "\n",
    "requirements = (['Health Screening',\n",
    "                 'Health Assessment',\n",
    "                 'Digital Coaching Program',\n",
    "                 'First Activity Campaign',\n",
    "                 'Second Activity Campaign'])\n",
    "print(requirement_lists)\n",
    "\n",
    "\n",
    "for idx in range(len(all_emails)):\n",
    "    name = all_names[idx]\n",
    "    email = all_emails[idx]\n",
    "    \n",
    "#     Created two lists completed and un_completed to differ what activites folks have completed and what activities they have not completed. Will use this to fill out the body of the email. \n",
    "    \n",
    "    completed = []\n",
    "    un_completed = []\n",
    "    \n",
    "    for i in range(len(requirements)):\n",
    "        completed_check(requirement_lists, i, requirements)\n",
    "    \n",
    "#     if all_health_screen[idx]=='Yes':\n",
    "#         completed.append('Health Screening')\n",
    "#     else:\n",
    "#         un_completed.append('Health Screening')\n",
    "        \n",
    "#     if all_health_assessment[idx]=='Yes':\n",
    "#         completed.append('Health Assessment')\n",
    "#     else:\n",
    "#         un_completed.append('Health Assessment')\n",
    "    \n",
    "#     if all_digital_coaching[idx]=='Yes':\n",
    "#         completed.append('Digital Coaching Program')\n",
    "#     else:\n",
    "#         un_completed.append('Digital Coaching Program')\n",
    "    \n",
    "#     if all_first_activity[idx]=='Yes':\n",
    "#         completed.append('First Activity Campaign')\n",
    "#     else:\n",
    "#         un_completed.append('First Activity Campaign')\n",
    "        \n",
    "#     if all_second_activity[idx]=='Yes':\n",
    "#         completed.append('Second Activity Campaign')\n",
    "#     else:\n",
    "#         un_completed.append('Second Activity Campaign')\n",
    "        \n",
    "    print(completed)\n",
    "    print(un_completed)\n",
    "        \n",
    "    if len(completed) == 5: \n",
    "        completed_string = \"\"\"You have completed all of the required activities for the health and wellness program. Thank you for participating in this program. Make sure to submit a receipt for reimbursement for passes or equipment.\"\"\"\n",
    "    elif len(completed) < 2:\n",
    "        completed_string = f\"\"\"As of today, you have completed {completed[0]}. Thank you for your efforts in order to complete these health and wellness initiatives.\"\"\"\n",
    "    else: \n",
    "        completed_items_string = ' '\n",
    "        for i in range(len(completed)):\n",
    "            if i < len(completed) - 2:\n",
    "                completed_items_string += \" \" + completed[i] + ','\n",
    "            elif i < len(completed) - 1:\n",
    "                completed_items_string += \" \" + completed[i] + ', and'\n",
    "            else:\n",
    "                completed_items_string += \" \" + completed[i] + '.'\n",
    "    \n",
    "    \n",
    "    full_list = []\n",
    "    full_list.append(name)\n",
    "    full_list.append(email)\n",
    "    full_list.append(completed)\n",
    "    full_list.append(un_completed)\n",
    "\n",
    "    \n",
    "    email_body = f\"\"\"Dear {name},\n",
    "    \n",
    "Thank you for being an active participant in Wasatch Academy’s Health and wellness program. In order to keep our benefits at the current level, we need 70% participation from faculty and staff. I wanted to reach out to update you on where you stand in this process. \n",
    "\n",
    "{completed_string}\n",
    "\n",
    "In order to qualify for the activity pass reimbursement or equipment reimbursement, you still need to complete {un_completed}. \n",
    "\n",
    "For more information on requirements and how to complete them, please visit this link.\n",
    "\n",
    "Please reach out to Michelle Prows if you have any questions regarding these requirements. \n",
    "\n",
    "Sincerely, \n",
    "The Health and Wellness Team\n",
    "\n",
    "    \n",
    "    \n",
    "    \"\"\"\n",
    "    print(email_body)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0c9329a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  cat, dog, and fish.\n"
     ]
    }
   ],
   "source": [
    "items = ['cat', 'dog', 'fish']\n",
    "completed_items_string = ' '\n",
    "for i in range(len(items)):\n",
    "    if i < len(items) - 2:\n",
    "        completed_items_string += \" \" + items[i] + ','\n",
    "    elif i < len(items) - 1:\n",
    "        completed_items_string += \" \" + items[i] + ', and'\n",
    "    else:\n",
    "        completed_items_string += \" \" + items[i] + '.'\n",
    "\n",
    "print(completed_items_string)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "79e92c5c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['All health screen completed']\n",
      "[]\n"
     ]
    }
   ],
   "source": [
    "completed = []\n",
    "un_completed = []\n",
    "\n",
    "completed_check(all_health_screen, 1, \"All health screen completed\")\n",
    "\n",
    "print(completed)\n",
    "print(un_completed)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f5def71",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
