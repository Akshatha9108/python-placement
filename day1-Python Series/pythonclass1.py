{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3ebdaae4-0e8c-4ab4-8364-6b60ceb18e0f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "a=5\n",
    "y=a+1\n",
    "print(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "00de3a54-eb08-4148-a56c-06149689ff8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "name=\"aksha\"\n",
    "print(\"d\" in name)#membership operator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d244a9a1-6908-40b0-9855-57d99ae5da9f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a=10\n",
    "b=10\n",
    "a is not b #identity operator\n",
    "a is b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "25e9d625-1c7d-440f-abde-f63090d5de74",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter 32\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "32\n",
      "<class 'int'>\n"
     ]
    }
   ],
   "source": [
    "age=int(input(\"enter\"))\n",
    "print(age)\n",
    "print(type(age))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7d91e261-8909-4799-a847-0da4ce98a002",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter 32\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[5], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m name\u001b[38;5;241m=\u001b[39m\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124menter\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m----> 2\u001b[0m age\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mint\u001b[39m(\u001b[38;5;28;43minput\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43menter\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m)\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmy name\u001b[39m\u001b[38;5;124m\"\u001b[39m,age)\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python311\\site-packages\\ipykernel\\kernelbase.py:1282\u001b[0m, in \u001b[0;36mKernel.raw_input\u001b[1;34m(self, prompt)\u001b[0m\n\u001b[0;32m   1280\u001b[0m     msg \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mraw_input was called, but this frontend does not support input requests.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1281\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m StdinNotImplementedError(msg)\n\u001b[1;32m-> 1282\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_input_request\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m   1283\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mstr\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mprompt\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1284\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_parent_ident\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mshell\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1285\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget_parent\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mshell\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1286\u001b[0m \u001b[43m    \u001b[49m\u001b[43mpassword\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m,\u001b[49m\n\u001b[0;32m   1287\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python311\\site-packages\\ipykernel\\kernelbase.py:1325\u001b[0m, in \u001b[0;36mKernel._input_request\u001b[1;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[0;32m   1322\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m:\n\u001b[0;32m   1323\u001b[0m     \u001b[38;5;66;03m# re-raise KeyboardInterrupt, to truncate traceback\u001b[39;00m\n\u001b[0;32m   1324\u001b[0m     msg \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInterrupted by user\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m-> 1325\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m(msg) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m   1326\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m:\n\u001b[0;32m   1327\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlog\u001b[38;5;241m.\u001b[39mwarning(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInvalid Message:\u001b[39m\u001b[38;5;124m\"\u001b[39m, exc_info\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter 32\n"
     ]
    }
   ],
   "source": [
    "name=input(\"enter\")\n",
    "age=int(input(\"enter\"))\n",
    "print(\"my name\",age)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "07571203-6768-4d42-96c3-cc1db82ff49a",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
